# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0003_auto_20170418_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topiccommentmodel',
            old_name='topic_id',
            new_name='topic',
        ),
    ]