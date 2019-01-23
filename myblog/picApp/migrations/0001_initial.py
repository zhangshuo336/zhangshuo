# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-23 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picTitle', models.CharField(max_length=20)),
                ('picContent', models.CharField(max_length=50)),
                ('picAddr', models.ImageField(upload_to=b'./')),
                ('picDate', models.DateTimeField(auto_now_add=True)),
                ('picIsDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
