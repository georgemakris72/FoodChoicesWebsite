# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 02:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20171223_0233'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='RestaurantLocation',
        ),
    ]
