# Generated by Django 2.1.5 on 2019-02-19 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_auto_20190219_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_chat',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 19, 15, 19, 24, 240582)),
        ),
    ]