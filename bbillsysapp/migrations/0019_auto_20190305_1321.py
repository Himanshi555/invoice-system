# Generated by Django 2.1.5 on 2019-03-05 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbillsysapp', '0018_auto_20190305_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_product',
            old_name='Sub_Category',
            new_name='SubCategory',
        ),
        migrations.RenameField(
            model_name='create_store',
            old_name='Sub_Category',
            new_name='SubCategory',
        ),
        migrations.AlterField(
            model_name='make_invoice',
            name='date_and_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 5, 13, 21, 22, 409034)),
        ),
    ]
