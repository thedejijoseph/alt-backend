from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class RootView(APIView):
    def get(self, request):
        return Response({
            'detail': 'This is a demo API Service.'
        })
