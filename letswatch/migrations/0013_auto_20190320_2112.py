# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2019-03-20 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letswatch', '0012_auto_20190320_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letswatch.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='watchlist',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='movieviews',
            unique_together=set([('movie', 'time_stamp')]),
        ),
    ]