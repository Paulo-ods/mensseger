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
            status, description, user = self.authenticate()

            if status:
                status, description, section = BO.coreBO.section.Section(user=user).access_section()

                response = {
                    'user_name': user.get('user'),
                    'user_token': user.get('token')
                }
                return status, description, response
            return False, 'Login not found', None
        except TypeError:
            return False, 'Login Error', None

    def authenticate(self):
        try:
            self.user = authenticate(username=self.username, password=self.password)

            if not self.user:
                return False, 'User Not Found', None
            response = {
                'token': self.create_token(request=self.request),
                'user': self.user
            }
            return True, '', response
        except TypeError:
            return False, 'Login user Error', None

    def create_token(self, request):
        try:
            payload = jwt_payload_handler(self.user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            user_logged_in.send(sender=self.user.__class__,
                                request=request, user=self.user)

            return token.decode('utf-8')
        except ValueError:
            return None

