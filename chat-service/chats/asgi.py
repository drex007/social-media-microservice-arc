import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chats.settings')
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application
asgi_server = get_asgi_application()


from channels.auth import AuthMiddlewareStack
import chatapp.routing


application = ProtocolTypeRouter({
  'http':get_asgi_application(),
  'websocket': AuthMiddlewareStack(
    URLRouter(
      chatapp.routing.websocket_urlpatterns
    )
  )
})