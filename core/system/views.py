from apiview.view import APIView
from django.http import JsonResponse
from django.shortcuts import render


class PermissionView(APIView):
    def get(self, *args, **kwargs):
        user_owner = self.request.GET.get('user_owner')
        response = {}

        return JsonResponse(response, safe=False)