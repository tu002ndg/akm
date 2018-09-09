# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-06 23:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0006_section_ordnum'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['group', 'ordnum'], 'verbose_name': 'секцию', 'verbose_name_plural': 'секции'},
        ),
        migrations.RemoveField(
            model_name='group',
            name='sections',
        ),
        migrations.AddField(
            model_name='section',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wiki.Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='ordnum',
            field=models.IntegerField(default='0', verbose_name='#'),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together=set([('group', 'ordnum')]),
        ),
    ]