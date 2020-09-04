

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from customer.models import Customer
from customer.validators import *

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['account', 'address']

class CreateCustomerSerializer(Serializer):
    username = serializers.CharField(
        max_length=100,
        validators=[unique_user_account]
    )
    password = serializers.CharField(
        max_length=100,
        validators=[common_password, strong_password]
    )
