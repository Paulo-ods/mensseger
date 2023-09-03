import telegram.views
from django.urls import re_path

urlpatterns = [
    re_path('home', telegram.views.TelegramView.as_view(), name='send_telegram'),
    re_path('send', telegram.views.SendMessageTelegramView.as_view(), name='send_telegram')
]