# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-14 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181014_2221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='pub_date_created',
            new_name='pub_date',
        ),
    ]
