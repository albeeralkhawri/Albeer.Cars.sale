# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-18 21:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Car_details',
            new_name='Car_detail',
        ),
    ]
