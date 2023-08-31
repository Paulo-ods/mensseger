from django.db import models
from django.urls import re_path

from whatsapp import views

# Create your models here.
urlpatterns = [
    re_path('enviar-mensagem', views.SendMessageView.as_view(), 'enviar_mensagem'),
]