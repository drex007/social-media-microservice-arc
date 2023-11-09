import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import ChatMessage



class ChatConsumers(AsyncWebsocketConsumer):
  async def connect(self):
  

    self.room_group_name = self.scope['url_route']['kwargs']['room_name']
    
    await self.channel_layer.group_add(
      self.room_group_name,self.channel_name
    )
    
    await self.accept()
    
  
  async def disconnect(self, code):
    #Leave group
    await self.channel_layer.group_discard(
      self.room_group_name,
      self.channel_name
    )
    
  #Receive message from websocket
  async def receive(self, text_data=None):
   
    data = json.loads(text_data)
    message = data['message']
    sender = data['sender']
    room = data['room']
    receiver = data['receiver'] 
    
    
    
    #save the message
    await self.save_message(room, sender, receiver, message)
    
    #Send message to group
    
    await self.channel_layer.group_send(
      self.room_group_name, {
        'type': 'chat_message',
        'message':message,
        'sender':sender  
      }
    )
  #Receive message from room group
  async def chat_message(self, event):
    message = event['message']
    sender = event['sender']
    
    
    #Sends message to websocket
    await self.send(text_data=json.dumps({
      'message':message,
      'sender': sender
      
    }))
  
  @sync_to_async
  def save_message(self, room, sender, receiver, content):
    ChatMessage.objects.create(chat_group = room, sender = sender, receiver =receiver, content = content)
    