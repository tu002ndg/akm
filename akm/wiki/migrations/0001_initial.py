# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-02 23:13
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='создана')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'группа шаблона',
                'ordering': ['title'],
                'verbose_name_plural': 'группы шаблонов',
            },
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordnum', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='заголовок')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'секция',
                'ordering': ['title'],
                'verbose_name_plural': 'секции',
            },
        ),
        migrations.AddField(
            model_name='pattern',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Section'),
        ),
        migrations.AddField(
            model_name='group',
            name='sections',
            field=models.ManyToManyField(through='wiki.Pattern', to='wiki.Section', verbose_name='секции'),
        ),
        migrations.AlterUniqueTogether(
            name='pattern',
            unique_together=set([('group', 'ordnum')]),
        ),
    ]
