# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-18 23:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20200118_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_detail',
            name='car',
        ),
        migrations.DeleteModel(
            name='Car_detail',
        ),
    ]