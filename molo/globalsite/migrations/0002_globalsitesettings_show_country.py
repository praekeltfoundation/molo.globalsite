# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-17 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsitesettings',
            name='show_country',
            field=models.BooleanField(default=False, help_text=b'When activated, the country name will be displayed and users will be able to change their country site.', verbose_name=b'Display Country'),
        ),
    ]
