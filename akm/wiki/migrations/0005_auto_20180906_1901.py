# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-06 16:01
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wiki', '0004_auto_20180904_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создана')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='изменена')),
                ('status', models.IntegerField(choices=[('1', 'Черновик'), ('2', 'Опубликована'), ('3', 'Архив')], default=1, verbose_name='статус')),
                ('view_count', models.IntegerField(default=0, verbose_name='просмотрена')),
                ('title', models.CharField(max_length=100, verbose_name='Название статьи')),
                ('abstract', models.TextField(verbose_name='краткое содержание (резюме)')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('uploaded', models.BooleanField(default=False, verbose_name='загружена?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name_plural': 'статьи',
                'verbose_name': 'статья',
                'ordering': ['category', '-modified'],
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordnum', models.IntegerField(verbose_name='#')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('markdown_content', models.TextField(verbose_name='содержание')),
                ('html_content', models.TextField(editable=False, verbose_name='html')),
                ('file_to', models.FileField(upload_to='', verbose_name='файл')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Article', verbose_name='статья')),
            ],
            options={
                'verbose_name_plural': 'содержание секции',
                'verbose_name': 'содержание секции',
                'ordering': ['ordnum'],
            },
        ),
        migrations.RemoveField(
            model_name='part',
            name='acronym',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=['part', 'title'], unique_with=('part',)),
        ),
        migrations.AlterField(
            model_name='part',
            name='slug',
            field=models.SlugField(max_length=5, unique=True, verbose_name='кратко'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Category', verbose_name='категория'),
        ),
        migrations.AlterUniqueTogether(
            name='detail',
            unique_together=set([('article', 'ordnum')]),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('category', 'title')]),
        ),
    ]