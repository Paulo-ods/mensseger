import json

import jwt
from django.contrib.auth import authenticate, login, user_logged_in
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
import user.user_login.models
from rest_framework_jwt.utils import jwt_payload_handler

from messenger import settings


class LoginUserView(APIView):
    def post(self, request):
        response = {'status': False, 'descricao': 'Login or Password not found'}
        data = json.loads(self.request.body)
        user = authenticate(username=data['username'], password=data['password'])
        user_details = {}

        # status = BO.funcionario.login.SessaoFuncionario.criar_sessao(self, user)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details['name'] = "%s %s" % (
                    user.nm_first, user.nm_last)
                user_details['token'] = token.decode('utf-8')
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)

                # empresa_user = BO.funcionario.login.Login.get_empresa(self, user)
                response = {
                    'user': user_details['name'],
                    'token': user_details['token'],
                    'first_screen': 'usuario',
                    'status': status.HTTP_200_OK

                }
                return JsonResponse(response, safe=False)
            except Exception as e:
                raise e
        return JsonResponse(response)


class RegisterUserView(APIView):
    # Classe temporaria, apenas para registrar pessoas momentaniamente
    def post(self, request):
        try:
            response = json.loads(self.request.body)
            username = f"{response['nm_first']}.{response['nm_last']}"
            newUser = user.user_login.models.UserLogin.objects.create_user(username=username,
                                                                           email=response['email'],
                                                                           password= response['password'],
                                                                           nm_first=response['nm_first'],
                                                                           nm_last=response['nm_last'])
            newUser.save()
            status = {'status': True}
        except:
            status ={'status': False}
        return JsonResponse(status)