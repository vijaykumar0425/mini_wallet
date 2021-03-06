# Generated by Django 3.2.7 on 2021-09-21 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_disabled', models.BooleanField(default=False)),
                ('disabled_at', models.DateTimeField(blank=True, null=True)),
                ('enabled_at', models.DateTimeField(blank=True, null=True)),
                ('owned_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
