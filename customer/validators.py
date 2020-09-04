
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.serializers import ValidationError

from customer.models import Customer


def unique_user_account(value):
    """
    When creating a customer account, confirm that another account
    has not been created with the same user profile. User profile is
    of type django.auth.User
    """
    try:
        account = User.objects.get(username=value)
        target_id = account.id
        try:
            customer = Customer.objects.get(account_id=target_id)
            raise ValidationError('Customer account for this user exists already.')
        except Customer.MultipleObjectsReturned:
            raise ValidationError('Customer acount for this user exists already.')
        except ObjectDoesNotExist:
            return value
    except ObjectDoesNotExist:
        # user profile has not been created
        return value

def common_password(value):
    pass

def strong_password(value):
    pass
