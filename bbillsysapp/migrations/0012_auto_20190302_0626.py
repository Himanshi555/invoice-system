# Generated by Django 2.1.5 on 2019-03-02 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbillsysapp', '0011_auto_20190302_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='make_invoice',
            name='date_and_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 6, 26, 40, 799710)),
        ),
    ]
