# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-11 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20160311_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ovedag',
            old_name='radmd5chksum',
            new_name='radmd5',
        ),
    ]
