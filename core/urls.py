from django.urls import include, re_path

import telegram.urls

urlpatterns = [
    re_path('telegram', include(telegram.urls), name='telegramBO'),
]