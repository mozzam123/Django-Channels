
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from .routing import websocket_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet.settings')


application = ProtocolTypeRouter({
    "websocket":  AuthMiddlewareStack(
        SessionMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        )
    ),
})
