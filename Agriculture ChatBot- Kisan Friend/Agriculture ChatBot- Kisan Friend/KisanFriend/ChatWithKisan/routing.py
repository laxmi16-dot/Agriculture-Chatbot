from django.urls import path
from .consumer import ConnectTOBot

websocket_urlpatterns = [
    path('ws/chat', ConnectTOBot.as_asgi()),
]

#This code defines WebSocket URL patterns for a Django Channels application. It specifies that WebSocket requests to the path **`ws/chat`** should be routed to the `ConnectTOBot` consumer, which is responsible for handling WebSocket connections, messages, and disconnections. The `as_asgi()` method ensures the consumer is compatible with the ASGI interface, enabling asynchronous communication. This setup is essential for mapping WebSocket endpoints to their corresponding consumers in a Django project.