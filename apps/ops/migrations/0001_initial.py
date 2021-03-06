# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-01 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('uuid', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='Name')),
                ('date_start', models.DateTimeField(auto_now_add=True, verbose_name='Start time')),
                ('date_finished', models.DateTimeField(blank=True, null=True, verbose_name='End time')),
                ('timedelta', models.FloatField(default=0.0, null=True, verbose_name='Time')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Is finished')),
                ('is_success', models.BooleanField(default=False, verbose_name='Is success')),
                ('assets', models.TextField(blank=True, null=True, verbose_name='Assets id')),
                ('_modules_args', models.TextField(blank=True, null=True, verbose_name='Task module and args json format')),
                ('pattern', models.CharField(default='all', max_length=64, verbose_name='Task run pattern')),
                ('result', models.TextField(blank=True, null=True, verbose_name='Task raw result')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='Task summary')),
            ],
        ),
    ]
