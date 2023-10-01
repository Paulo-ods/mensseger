from django.urls import include, re_path

import telegram.urls
import core.login.urls

urlpatterns = [
    re_path('', include(core.login.urls), name='login'),
    re_path('api/telegram', include(telegram.urls), name='telegram'),
    re_path('api/system', include(telegram.urls), name='system'),
]