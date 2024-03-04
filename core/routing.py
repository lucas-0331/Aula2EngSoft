from django.urls import re_path
from core.consumers import OrderConsumer, KitchenConsumer

websocket_urlpatterns = [
    re_path(r'ws/order/$', OrderConsumer.as_asgi()),
    re_path(r'ws/kitchen/$', KitchenConsumer.as_asgi()),
]
