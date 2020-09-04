
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from customer.serializers import CustomerSerializer, CreateCustomerSerializer
from customer.models import Customer


class RootView(APIView):
    def get(self, request):
        return Response({
            'detail': 'Customer API Service'
        })

class CustomerSignup(APIView):
    def post(self, request):
        serializer = CreateCustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # if a user account exists with these credentials already,
        # authenticate with credentials
        account = authenticate(
            username=data['username'],
            password=data['password']    
        )
        user_account_mesage = 'User profile exists already. '

        if not account:
            account = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            user_account_mesage = ''
        
        customer = Customer.objects.create(account=account)
        token = Token.objects.create(user=account)

        return Response(
            {
                'detail': f'{user_account_mesage}Customer account created successfully',
                'token': token.key
            },
            status = status.HTTP_201_CREATED
        )
