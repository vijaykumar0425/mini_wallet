import uuid
from django.db import models
from accounts.models import User
from decimal import Decimal
from django.db import transaction, IntegrityError
# Create your models here.


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_disabled = models.BooleanField(default=False)
    disabled_at = models.DateTimeField(null=True, blank=True)
    enabled_at = models.DateTimeField(null=True, blank=True)
    owned_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')

    @transaction.atomic
    def deposit(self, amount):
        amount = Decimal(amount)

        self.transaction_set.create(
            amount=amount,
            running_balance=self.balance + amount
        )
        self.balance += amount
        self.save()

    @transaction.atomic
    def withdraw(self, amount):
        amount = Decimal(amount)
        if amount > self.balance:
            raise IntegrityError("Insufficient Balance")

        self.transaction_set.create(
            amount=-amount,
            running_balance=self.balance - amount
        )
        self.balance -= amount
        self.save()


