# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-05-19 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0002_auto_20170519_1100'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LatestNews',
            new_name='News',
        ),
    ]
