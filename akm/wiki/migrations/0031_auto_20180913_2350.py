# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0030_auto_20180913_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=100, verbose_name='заголовок'),
        ),
    ]
