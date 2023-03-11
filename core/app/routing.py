from django.urls import path
from app import consumers
from app.consumers import *
websocket_urlpatterns=[
    # path('ws/sc/', consumers.MySyncConsumer.as_view()),
    # path('ws/ac/', consumers.MyAsyncConsumer.as_view()),
    ]