

"""
And now, we implement our own validators.
The default ModelSerializer when trying to create a new merchant account
tries to validate uniqueness based on the User object. We need the
uniqueness to be on the Merchant onject

That is, if a Merchant object has been created with that account before,
we raise an error.

"""

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from rest_framework.serializers import ValidationError

from merchant.models import Merchant


def unique_user_account(value):
    # first confirm that user profile exists
    try:
        account = User.objects.get(username=value)
        target_id = account.id
        try:
            merchant = Merchant.objects.get(account_id=target_id)
            raise ValidationError('Merchant account for this user already exists.')
        except Merchant.MultipleObjectsReturned:
            raise ValidationError('Merchant account for this user already exists.')
        except ObjectDoesNotExist:
            # merchant account with user id does not exist
            return value
    except ObjectDoesNotExist:
        # user account does not exist
        return value