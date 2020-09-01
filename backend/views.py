
from rest_framework.views import APIView
from rest_framework.response import Response

class RootView(APIView):
    def get(self, request):
        return Response({
            'detail': 'The Alternate Backend Service',
            'root': '/ - You are at root',
            'merchants': '/merchant/ - Merchants endpoint'
        })
