# Generated by Django 2.1.5 on 2019-03-06 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0008_auto_20190306_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_chat',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 6, 15, 36, 11, 961683)),
        ),
    ]
