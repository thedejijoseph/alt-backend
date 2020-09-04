
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from merchant.validators import *
from merchant.models import Merchant

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CreateMerchantSerializer(Serializer):
    username = serializers.CharField(
        max_length=40,
        validators=[unique_user_account]
    )
    password = serializers.CharField(max_length=100)

    def validate_password(self, value):
        """
        We could check that the password has A, a, 1, and #
        kinda sturvs...
        """
        # raise ValidationError
        return value

