
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from app.routing import websocket_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet.settings')


application = ProtocolTypeRouter({
    "websocket":  AuthMiddlewareStack(
        SessionMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        )
    ),
})
