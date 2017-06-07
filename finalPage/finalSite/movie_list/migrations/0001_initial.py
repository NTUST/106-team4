# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-05-19 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctitle', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('director', models.CharField(default='無', max_length=100)),
                ('actors', models.TextField(default='無')),
                ('length', models.CharField(default='2小時', max_length=20)),
                ('movietype', models.CharField(default='動畫', max_length=100)),
                ('videourl', models.URLField(default='www.youtube.com')),
                ('introduction', models.TextField(default='電影介紹')),
                ('pub_date', models.DateField(verbose_name='上映日期')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_list.Category')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
