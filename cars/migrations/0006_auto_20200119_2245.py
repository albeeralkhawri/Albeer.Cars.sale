# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-19 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_detail',
            name='image1',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='car_detail',
            name='image2',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='car_detail',
            name='image3',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
