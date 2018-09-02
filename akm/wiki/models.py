from django.db import models
from django.contrib.auth import models as auth_models
import datetime

''' Секция статьи '''
class Section(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100,unique=True,
    verbose_name='заголовок')
    description = models.TextField(verbose_name='описание')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='секцию'
        verbose_name_plural='секции'
        ordering=['title']

''' Группа шаблона '''
class Group(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(auth_models.User,verbose_name='автор')
    created = models.DateTimeField(default=datetime.datetime.now,
    verbose_name='создана')
    title = models.CharField(max_length=100, unique=True,
    verbose_name='название')
    description = models.TextField(verbose_name='описание')
    sections = models.ManyToManyField(Section, 
    through='Pattern',through_fields=('group','section'),
    verbose_name='секции')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='группа шаблона'
        verbose_name_plural='группы шаблонов'
        ordering=['title']

''' Шаблон статьи'''
class Pattern(models.Model):
    objects = models.Manager()
    group = models.ForeignKey(Group)
    section = models.ForeignKey(Section)
    ordnum = models.IntegerField()
    verbose_name='№'
    class Meta:
        unique_together = ['group','ordnum']


