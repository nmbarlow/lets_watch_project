# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2019-03-20 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letswatch', '0004_auto_20190320_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.TextField(),
        ),
    ]
