# Generated by Django 2.0.3 on 2019-02-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190224_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='suborder',
            name='extra_cheese',
            field=models.BooleanField(default=False),
        ),
    ]
