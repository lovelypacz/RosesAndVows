# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-13 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_auto_20180114_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_validated',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
