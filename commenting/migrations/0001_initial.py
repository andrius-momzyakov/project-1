# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-26 15:49
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='\u041a\u043e\u0433\u0434\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u043e')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='\u041a\u043e\u0433\u0434\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u043e')),
                ('commenter_email', models.EmailField(max_length=254, verbose_name='\u0412\u0430\u0448 e-mail@mts.ru')),
                ('commenter_name', models.CharField(max_length=250, verbose_name='\u0412\u0430\u0448\u0435 \u0438\u043c\u044f')),
                ('body', ckeditor.fields.RichTextField(max_length=2000, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f (<=2000 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432)')),
                ('parent_url', models.CharField(max_length=2048, verbose_name='Url \u0434\u043b\u044f \u043f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 (<=2048 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432)')),
                ('confirmation_token', models.CharField(max_length=32, unique=True, verbose_name='\u041a\u043b\u044e\u0447 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('is_active', models.BooleanField(verbose_name='\u0417\u0430\u043f\u0438\u0441\u044c \u0430\u043a\u0442\u0438\u0432\u043d\u0430')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmmnt_creator', to=settings.AUTH_USER_MODEL, verbose_name='\u041a\u0435\u043c \u0441\u043e\u0437\u0434\u0430\u043d\u043e')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmmnt_updater', to=settings.AUTH_USER_MODEL, verbose_name='\u041a\u0435\u043c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u043e')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439',
                'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438',
            },
        ),
    ]
