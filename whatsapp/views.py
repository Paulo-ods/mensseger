from django.http import JsonResponse
from rest_framework.views import APIView

import BO.whatsappBO.whatsapp


class SendMessageView(APIView):
    def get(self, *args, **kwargs):
        status, description = BO.whatsapp.whatsapp.WhatsappBO.send_mensage()

        response = {
            'status': status,
            'description': description
        }

        return JsonResponse(response, safe=False)