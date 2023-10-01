import json

import jwt
from django.contrib.auth import authenticate, login, user_logged_in
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

import BO.coreBO.login
import user.user_login.models
from rest_framework_jwt.utils import jwt_payload_handler

from messenger import settings


class LoginUserView(APIView):
    def post(self, request):
        data = json.loads(self.request.body)

        status, description, response = BO.coreBO.login.Login(request=self.request,
                                                              username=data.get('username'),
                                                              password=data.get('password')).login()
        response = {
            'status': status,
            'description': description,
            'response': response
        }
        return JsonResponse(response)


class RegisterUserView(APIView):
    # Classe temporaria, apenas para registrar pessoas momentaniamente
    def post(self, request):
        try:
            response = json.loads(self.request.body)
            username = f"{response['nm_first']}.{response['nm_last']}"
            newUser = user.user_login.models.UserLogin.objects.create_user(username=username,
                                                                           email=response['email'],
                                                                           password=response['password'],
                                                                           nm_first=response['nm_first'],
                                                                           nm_last=response['nm_last'])
            newUser.save()
            status = {'status': True}
        except:
            status = {'status': False}
        return JsonResponse(status)
