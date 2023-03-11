"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.security.websocket import AllowedHostsOriginValidator
from app.consumers import TextConsumer
from channels.auth import AuthMiddlewareStack
from core import app
# import app.routing
from app import routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# application = get_asgi_application()

# ws_patterns = [
#     path('ws/test/',TextConsumer )
# ]

application = ProtocolTypeRouter({
    # 'websocket': URLRouter(app.routing.websocket_urlpatterns),
    'http':get_asgi_application(),
    "websocket":AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(app.routing.websocket_urlpatterns)),
    )
    
})



# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     # Just HTTP for now. (We can add other protocols later.)
# })