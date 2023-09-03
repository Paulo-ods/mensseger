from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import render
import requests

import BO.telegramBO.telegram
import core.models


class TelegramView(APIView):

    def get(self, *args, **kwargs):
        context = {
            'message': core.models.Config.objects.filter(code='html').values('description').first()
        }

        return render(self.request, 'home.html', context)


# Create your views here.
class SendMessageTelegramView(APIView):

    def get(self, *args, **kwargs):
        status, description, data = BO.telegramBO.telegram.TelegramBO().send_messenge_telegram()
        response = {
            'status': True,
            'descricao': description,
            'data': None
        }

        return JsonResponse(response, safe=True)
