# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2019-03-19 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letswatch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
