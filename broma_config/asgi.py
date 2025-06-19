import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "broma_config.settings.local")

# HTTP-приложение Django
django_asgi_app = get_asgi_application()

# Импорты для WebSocket
from channels.routing import ProtocolTypeRouter, URLRouter
import conversations.routing
from conversations.middlewares import ConversationUserSessionMiddlewareStack

# Объединённый ASGI application
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": ConversationUserSessionMiddlewareStack(
        URLRouter(
            conversations.routing.websocket_urlpatterns
        )
    ),
})
