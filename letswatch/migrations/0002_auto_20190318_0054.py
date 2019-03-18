# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2019-03-18 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letswatch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='picture',
            field=models.ImageField(blank=True, default='profile_images/default.png', upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='movie',
            name='thumb',
            field=models.ImageField(blank=True, upload_to='movies'),
        ),
    ]
