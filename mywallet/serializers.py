from rest_framework import serializers
from .models import Wallet
from django.utils import timezone


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('is_disabled')
        ret["status"] = "disabled" if instance.is_disabled else "enabled"
        return ret

    def save(self, **kwargs):
        if self.validated_data.get('is_disabled') and self.instance.is_disabled is False:
            self.instance.disabled_at = timezone.now()
        return super().save(**kwargs)
