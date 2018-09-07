# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 16:32
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wiki', '0003_auto_20180904_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='создана')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='категория')),
                ('importance', models.IntegerField(default=0, verbose_name='(!)')),
                ('description', models.TextField(verbose_name='описание')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('part',))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name_plural': 'категории',
                'ordering': ['importance', 'title'],
                'verbose_name': 'категория',
            },
        ),
        migrations.AlterField(
            model_name='part',
            name='title',
            field=models.CharField(max_length=25, unique=True, verbose_name='раздел'),
        ),
        migrations.AddField(
            model_name='category',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Part', verbose_name='раздел'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('part', 'title')]),
        ),
    ]
