from django.shortcuts import render
from .models import ChatMessage
# Create your views here.
def index(request, chat_group):
  messages = []

  chat = ChatMessage.objects.filter(chat_group = chat_group).first()
  if (chat):
    messages = ChatMessage.objects.filter(chat_group = chat_group)
    return render(request, 'chatapp/index.html', {'messages': messages})
  else:
    return render(request, 'chatapp/index.html', {'messages': messages})
  
  
def paymentFunction(admission:int):
  return admission