# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
