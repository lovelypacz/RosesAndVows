# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-12 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_auto_20180111_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='package_images/'),
        ),
    ]
