# Generated by Django 2.1.5 on 2019-03-06 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbillsysapp', '0020_merge_20190305_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='make_invoice',
            name='date_and_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 6, 15, 20, 18, 7686)),
        ),
    ]
