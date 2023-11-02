from django.shortcuts import render
from rest_framework.views import APIView
from .models import PostModel
from .serializers import PostSerializers
from rest_framework.response import Response
# Create your views here.


class PostView(APIView):
  serializer_class = PostSerializers
  def get(self, request):
    objs = PostModel.objects.all()
    serializer = self.serializer_class(objs, many=True)
    return Response(data= serializer.data)
  def post(self, request):
    data = request.data
    serializer = self.serializer_class(data=data)
    if serializer.is_valid():
      serializer.save()
    return Response(data=serializer.data)
  
  

class PostView2(APIView):
  serializer_class = PostSerializers
  def get(self, request):
    objs = PostModel.objects.all()
    serializer = self.serializer_class(objs, many=True)
    return Response(data= serializer.data)
 