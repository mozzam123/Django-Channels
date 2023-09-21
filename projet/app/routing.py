from django.urls import path
from app.consumers import MyConsumer


websocket_urlpatterns = [
    path('ws/v1/', MyConsumer.as_asgi()),
]
