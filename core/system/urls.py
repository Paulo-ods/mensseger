from django.urls import re_path
from core.system import views
urlpatterns = [
    re_path('permissionAll', views.PermissionView, name='permission')
]