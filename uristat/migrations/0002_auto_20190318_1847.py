# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-18 15:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uristat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='followlog',
            options={'verbose_name': '\u041f\u0435\u0440\u0435\u0445\u043e\u0434 \u043f\u043e \u0441\u0441\u044b\u043b\u043a\u0435', 'verbose_name_plural': '\u041f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u043f\u043e \u0441\u0441\u044b\u043b\u043a\u0430\u043c'},
        ),
        migrations.AlterField(
            model_name='followlog',
            name='log_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 18, 47, 41, 537000), verbose_name='\u0412\u0440\u0435\u043c\u044f \u0444\u0438\u043a\u0441\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='followlog',
            name='session_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Id \u0441\u0435\u0441\u0441\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 18, 47, 41, 537000), verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0440\u0430\u0441\u0447\u0435\u0442\u0430'),
        ),
    ]
