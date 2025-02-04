import os
import django
from django.core.asgi import get_asgi_application
from whitenoise import WhiteNoise
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'morsechat.settings')

django.setup()

from room import routing

django_asgi_app = get_asgi_application()
django_asgi_app = WhiteNoise(django_asgi_app)

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
})
