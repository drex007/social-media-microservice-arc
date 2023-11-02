from django.urls import path
from .views import *

urlpatterns = [
    path('', PostView.as_view(), name='post'),
    path('all', PostView2.as_view(), name='post-2'),
    
]
