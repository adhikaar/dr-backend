# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-03 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_deviceid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='deviceId',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
