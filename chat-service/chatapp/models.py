from django.db import models

# Create your models here.


class ChatMessage(models.Model):
  chat_group = models.CharField(max_length=255, null=True, blank=True)
  sender = models.CharField(max_length=10, null=True, blank=True)
  receiver = models.CharField(max_length=10, null=True, blank=True)
  content =  models.CharField(max_length=10, null=True, blank=True)
  date = models.DateField(auto_now=True)
  
  
  def __str__(self):
    return f"{self.sender} || {self.receiver}"