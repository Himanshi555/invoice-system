# Generated by Django 2.1.5 on 2019-03-02 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0006_auto_20190228_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_chat',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 2, 6, 26, 11, 918914)),
        ),
    ]