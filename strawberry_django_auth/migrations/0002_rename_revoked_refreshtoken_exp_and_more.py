# Generated by Django 4.2.4 on 2023-08-21 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strawberry_django_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refreshtoken',
            old_name='revoked',
            new_name='exp',
        ),
        migrations.RenameField(
            model_name='refreshtoken',
            old_name='created',
            new_name='iat',
        ),
    ]
