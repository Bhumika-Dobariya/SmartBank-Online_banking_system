# Generated by Django 5.1 on 2024-08-29 05:40

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('offer_type', models.CharField(choices=[('discount', 'Discount'), ('cashback', 'Cashback'), ('buy_one_get_one', 'Buy One Get One'), ('free_trial', 'Free Trial'), ('other', 'Other')], max_length=20)),
                ('discount_percentage', models.PositiveIntegerField(blank=True, null=True)),
                ('cashback_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('valid_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_until', models.DateTimeField()),
                ('applicable_to', models.CharField(max_length=50)),
                ('entity_id', models.UUIDField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
