# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-12 14:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_auto_20160312_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='øvedage',
            name='radmd5',
        ),
    ]
