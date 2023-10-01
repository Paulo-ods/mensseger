from typing import Optional

import jwt
from django.contrib.auth import authenticate, user_logged_in
from rest_framework_jwt.utils import jwt_payload_handler

import BO.coreBO.section
from messenger import settings


class Login:
    def __init__(self, request=None, username=None, password=None):
        self.request = request
        self.username = username
        self.password = password
        self.user = None

    def login(self):
        try:
            status, description, user = self.autenticate()

            if status:
                status, description, section = BO.coreBO.section.Section(user=user).do()


                response = {
                    'user_name': user.get('user'),
                    'user_token': user.get('token')
                }
                return status, description, response
        except TypeError:
            return False, 'Login Error', None

    def autenticate(self):
        try:
            self.user = authenticate(username=self.username, password=self.password)

            if self.user:
                status, description, response = self.create_token(request=self.request)
            return status, description, response
        except TypeError:
            return False, 'Login user Error', None

    def create_token(self, request):
        try:
            user_details = {}
            payload = jwt_payload_handler(self.user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            user_logged_in.send(sender=self.user.__class__,
                                request=request, user=self.user)

            response = {
                'user': "%s %s" % (self.user.nm_first, self.user.nm_last),
                'token': token.decode('utf-8'),

            }
        except ValueError:
            return False, 'Token Error', None

