# Generated by Django 2.1.3 on 2019-02-28 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbillsysapp', '0009_auto_20190225_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='make_invoice',
            name='date_and_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 28, 12, 44, 8, 298166)),
        ),
    ]
