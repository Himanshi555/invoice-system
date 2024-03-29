# Generated by Django 2.1.5 on 2019-03-05 05:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbillsysapp', '0015_auto_20190303_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='create_brand/')),
            ],
        ),
        migrations.CreateModel(
            name='create_store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.PositiveIntegerField()),
                ('Title', models.CharField(max_length=255)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='create_store/')),
                ('Store_description', models.TextField(max_length=255)),
                ('Details', models.TextField(max_length=255)),
                ('Meta_Title', models.CharField(max_length=128)),
                ('Meta_Keyword', models.CharField(max_length=128)),
                ('Meta_Desc', models.CharField(max_length=128)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbillsysapp.Prod_Category')),
                ('Sub_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbillsysapp.Prod_subcategory')),
                ('select_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbillsysapp.create_brand')),
            ],
        ),
        migrations.AlterField(
            model_name='make_invoice',
            name='date_and_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 5, 10, 47, 34, 162468)),
        ),
    ]
