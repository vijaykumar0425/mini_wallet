from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Customer, User
from mywallet.models import Wallet


@receiver(post_save, sender=User)
def customer_wallet_create(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
        Wallet.objects.create(owned_by=instance)
