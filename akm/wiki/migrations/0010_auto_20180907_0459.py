# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-07 01:59
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0009_auto_20180907_0220'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pattern',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='pattern',
            name='group',
        ),
        migrations.RemoveField(
            model_name='pattern',
            name='section',
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['title'], 'verbose_name': 'шаблон', 'verbose_name_plural': 'шаблоны'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['group', 'ordnum'], 'verbose_name': 'секция', 'verbose_name_plural': 'секции'},
        ),
        migrations.RenameField(
            model_name='part',
            old_name='image',
            new_name='logo',
        ),
        migrations.AddField(
            model_name='part',
            name='acronym',
            field=models.CharField(default='genius', max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='создан'),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(verbose_name='примечание'),
        ),
        migrations.AlterField(
            model_name='part',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=10, populate_from=['acronym'], unique=True, verbose_name='кратко'),
        ),
        migrations.AlterField(
            model_name='part',
            name='title',
            field=models.CharField(max_length=25, verbose_name='раздел'),
        ),
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.TextField(verbose_name='примечание'),
        ),
        migrations.DeleteModel(
            name='Pattern',
        ),
    ]