from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/conversations/(?P<id>[0-9a-f\-]+)/$", consumers.ConversationConsumer.as_asgi()),
]
