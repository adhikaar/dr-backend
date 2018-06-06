# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-29 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20180528_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='intro_text',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='specialization',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]