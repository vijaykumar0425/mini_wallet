from rest_framework import serializers
from .models import Wallet
from accounts.models import User
from rest_framework.authtoken.models import Token


class AccountInitializeSerializer(serializers.Serializer):
    customer_xid = serializers.UUIDField()

    def create_user_token(self):
        try:
            user = User.objects.get(id=self.customer_xid)
            Token.objects.filter(user=user).delete()

            token = Token.objects.get_or_create(user=user)
            return token[0]
        except User.DoesNotExist:
            return None


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"
