# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-04 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_qrhash'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='qrhash_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
