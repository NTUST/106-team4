# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-05-22 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('phonenumber', models.CharField(max_length=20)),
                ('content', models.TextField(default='無')),
            ],
        ),
    ]
