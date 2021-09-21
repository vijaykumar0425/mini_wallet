from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import User, Customer


class AccountInitializeSerializer(serializers.Serializer):
    customer_xid = serializers.UUIDField()

    def create_user_token(self):
        try:
            token = Token.objects.get_or_create(user=self.instance.user)
            return token[0].key
        except User.DoesNotExist:
            return None

    def validate_customer_xid(self, customer_xid):
        try:
            customer = Customer.objects.get(user__id=customer_xid)
            self.instance = customer
        except Customer.DoesNotExist:
            raise serializers.ValidationError("Account Not Register Yet")
        return customer_xid
