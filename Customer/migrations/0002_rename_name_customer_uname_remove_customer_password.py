# Generated by Django 5.1 on 2024-08-31 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='uname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
    ]
