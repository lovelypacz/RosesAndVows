# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-11 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20171227_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='package_images'),
        ),
    ]
