from django.urls import path, re_path, include
from django.views.decorators.csrf import csrf_exempt

import core.login.views

urlpatterns = [
    re_path('login', csrf_exempt(core.login.views.LoginUserView.as_view()), name='login'),
    re_path('register', csrf_exempt(core.login.views.RegisterUserView.as_view()), name='cadastrar'),
]
