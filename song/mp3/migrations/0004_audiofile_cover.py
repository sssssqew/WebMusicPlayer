# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-31 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp3', '0003_remove_audiofile_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='cover',
            field=models.ImageField(default='mp3/static/mp3/cover3.png', upload_to='mp3/static/albumCover'),
        ),
    ]