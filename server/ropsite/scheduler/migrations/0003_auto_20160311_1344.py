# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-11 13:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20160311_1334'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Øvedag',
            new_name='Ovedag',
        ),
        migrations.RenameField(
            model_name='lokaler',
            old_name='øvedag',
            new_name='ovedag',
        ),
    ]