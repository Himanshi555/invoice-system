# Generated by Django 2.1.5 on 2019-02-25 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_auto_20190219_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_chat',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 4, 15, 5, 820288)),
        ),
    ]
