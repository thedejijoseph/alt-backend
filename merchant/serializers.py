from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

