from django.views.decorators.csrf import csrf_exempt

import telegram.views
from django.urls import re_path

urlpatterns = [
    re_path('', csrf_exempt(telegram.views.WebHookTelegramView.as_view()), name='webhook_telegram'),
    re_path('home', telegram.views.TelegramView.as_view(), name='send_telegram'),
    re_path('send', telegram.views.SendMessageTelegramView.as_view(), name='send_telegram')
]