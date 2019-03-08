# Generated by Django 2.1.5 on 2019-03-05 05:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbillsysapp', '0016_auto_20190305_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_store',
            name='select_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbillsysapp.Prod_Brand'),
        ),
        migrations.AlterField(
            model_name='make_invoice',
            name='date_and_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 5, 10, 59, 53, 480976)),
        ),
        migrations.DeleteModel(
            name='create_brand',
        ),
    ]
