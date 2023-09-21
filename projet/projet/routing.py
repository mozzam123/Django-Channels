from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app.consumers import MyConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/v1/", MyConsumer.as_asgi()),
    ]),
})
