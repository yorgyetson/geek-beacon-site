# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-25 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_menuitem_override_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurehistory',
            name='image',
            field=models.ImageField(blank=True, upload_to='content/featured/'),
        ),
    ]
