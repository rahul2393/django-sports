# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_auto_20171205_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='creatorId',
            new_name='creator',
        ),
    ]
