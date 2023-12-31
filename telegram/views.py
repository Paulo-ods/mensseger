from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests

import BO.telegramBO.telegram
import core.models


class TelegramView(APIView):

    def get(self, *args, **kwargs):
        self.request.GET.get('user_id')
        response = {
            'message': core.models.Config.objects.filter(code='html').values('description').first()
        }

        return JsonResponse(response, safe=False)


# Create your views here.
class SendMessageTelegramView(APIView):

    def get(self, *args, **kwargs):
        status, description, data = BO.telegramBO.telegram.TelegramBO().send_messenge_telegram(category='test_message')
        response = {
            'status': True,
            'descricao': description,
            'data': None
        }

        return JsonResponse(response, safe=True)


class WebHookTelegramView(APIView):
    def post(self, *args, **kwargs):
        print(self.request.data)
        status, description, data = BO.telegramBO.telegram.TelegramBO().send_messenge_welcome_telegram(
            category='welcome_message', data=self.request.data
        )

        return HttpResponse({'status': 'true', 'messege': 'worked'})
