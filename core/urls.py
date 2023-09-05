from django.urls import include, re_path

import telegram.urls
import core.login.urls

urlpatterns = [
    re_path('', include(core.login.urls), name='login'),
    re_path('telegram', include(telegram.urls), name='telegramBO'),
]