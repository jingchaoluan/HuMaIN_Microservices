# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170705_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameters',
            name='model',
            field=models.FileField(help_text='the reconizor model used in recongnition servie', null=True, upload_to=''),
        ),
    ]