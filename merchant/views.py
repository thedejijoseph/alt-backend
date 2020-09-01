from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import UserSerializer

class RootView(APIView):
    def get(self, request):
        return Response({
            'detail': 'Merchant API Service.'
        })

class UserSignup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # if serializer data is validated, create a new user
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        token = Token.objects.create(user=user)

        return Response(
            {
                'detail': 'User created successfully',
                'token': token.key
            },
            status = status.HTTP_201_CREATED
        )

class UserLogin(APIView):
    def post(self, request):
        data = request.data

        # authenticate user credentials
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if user:
            token = Token.objects.get(user=user)
            return Response(
                {
                    'token': token.key
                },
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'detail': 'Invalid credentials'
                },
                status = status.HTTP_400_BAD_REQUEST
            )
