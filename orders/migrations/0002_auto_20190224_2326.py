# Generated by Django 2.0.3 on 2019-02-24 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='pending_orders',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='shooping_cart',
        ),
    ]
