# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2019-03-20 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letswatch', '0010_auto_20190320_0747'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([]),
        ),
    ]
