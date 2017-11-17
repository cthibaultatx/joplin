# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('hours', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=255)),
                ('director_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('address', models.CharField(max_length=255)),
                ('event_fees', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
