from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify


''' Группа шаблона '''
class Group(models.Model):
    objects = models.Manager()
    author = models.ForeignKey('auth.User', verbose_name='автор',)
    created = models.DateTimeField(default=timezone.now,
    verbose_name='создан')
    title = models.CharField(max_length=100, unique=True,
    verbose_name='название')
    description = models.TextField(verbose_name='примечание')
    #sections = models.ManyToManyField(Section,
    #through='Pattern',
    #through_fields=('group','section'),
    #verbose_name='секции')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='шаблон'
        verbose_name_plural='шаблоны'
        ordering=['title']


''' Секция шаблона статьи '''
class Section(models.Model):
    objects = models.Manager()
    group = models.ForeignKey(Group)
    ordnum = models.IntegerField(verbose_name='#', default='0')
    title = models.CharField(max_length=100, verbose_name='заголовок')
    description = models.TextField(blank=True, verbose_name='примечание')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='секция'
        verbose_name_plural='секции'
        unique_together = ['group','ordnum']
        ordering=['group', 'ordnum']




#''' Шаблон статьи'''
#class Pattern(models.Model):
#    objects = models.Manager()
#    group = models.ForeignKey(Group)
#    ordnum = models.IntegerField(verbose_name='№')
#    section = models.ForeignKey(Section, verbose_name='секция')
#    def __str__(self):
#        return ''
#    class Meta:
#        verbose_name='секционный раздел в шаблоне'
#        verbose_name_plural='шаблон статьи wiki'
#        unique_together = ['group','ordnum']
#        ordering=['ordnum']

''' Раздел  WIKI '''
class Part(models.Model):    
    objects = models.Manager()
    author = models.ForeignKey('auth.User', verbose_name='автор',)
    created = models.DateTimeField(default=timezone.now,
    verbose_name='создан')
    #patterns = models.ManyToManyField(Group,through='Pattern', 
    #through_fields=('part','group'), verbose_name='шаблоны')
    pattern = models.ForeignKey(Group, verbose_name='шаблон')
    acronym = models.CharField(max_length=15,unique=True, 
    verbose_name='краткое')
    title = models.CharField(max_length=30, verbose_name='полное')
    importance = models.IntegerField(default = 0, verbose_name="(!)")
    description = models.TextField(verbose_name='описание') 
    slug = AutoSlugField(max_length = 15, unique=True, populate_from='acronym')
    logo = models.ImageField(upload_to = "wiki/part", verbose_name = "Логотип")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='раздел'
        verbose_name_plural='разделы'
        ordering=['importance','title']        

''' Категории статей в разделе Wiki '''
class Category(models.Model):    
    objects = models.Manager()
    author = models.ForeignKey('auth.User', verbose_name='автор',)
    created = models.DateTimeField(default=timezone.now,
    verbose_name='создана')
    part = models.ForeignKey(Part, verbose_name="раздел")
    title = models.CharField(max_length=50, unique=True,
    verbose_name='категория')
    importance = models.IntegerField(default = 0, verbose_name="(!)")
    description = models.TextField(verbose_name='описание')
    slug = AutoSlugField(max_length = 50, populate_from='title', 
    db_index=True,unique_with='part')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='категория'
        verbose_name_plural='категории'
        ordering=['importance','title']
        unique_together = ['part','title']


''' Статья Wiki '''

class PublishedArticlesManager(models.Manager):
    def get_query_set(self):
        return super(PublishedArticlesManager, self).get_query_set().filter(status=1)


STATUS_CHOICES = ((0, 'Черновик'),(1, 'Опубликована'),(2, 'Архив'),)

class Article(models.Model):    
    objects = models.Manager()
    published = PublishedArticlesManager()

    author = models.ForeignKey('auth.User', verbose_name='автор',)
    created = models.DateTimeField(auto_now_add=True,
    verbose_name='создана')
#    modified = models.DateTimeField(auto_now=True,
#    verbose_name='изменена')
#    modified_by = models.ForeignKey('auth.User', verbose_name='редактор',
#    related_name='+')    
    status = models.IntegerField(choices = STATUS_CHOICES, 
    default = 0, verbose_name='статус')
    view_count = models.IntegerField(default = 0, verbose_name="просмотрена")
    category = models.ForeignKey(Category, verbose_name="категория")
    title = models.CharField(max_length=100,verbose_name='Название статьи')
    abstract = models.TextField(verbose_name='краткое содержание (резюме)')
    slug = models.SlugField(max_length = 100, unique=True)
    uploaded = models.BooleanField(verbose_name="загружена?", default = False)
    
    def __str__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('wiki_article_detail', (), {'pk': self.pk })

    class Meta:
        verbose_name='статью'
        verbose_name_plural='статьи'
        ordering=['category']
        unique_together = ['category','title']

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = '{0}/{1}/{2}'.format(self.category.part.slug, 
            self.category.slug, str(self.id))
            self.save()
        


''' Содержание (секции) статьи '''
class Detail(models.Model):
    objects = models.Manager()
    article = models.ForeignKey(Article, verbose_name="статья", 
    on_delete = models.CASCADE)
    ordnum = models.IntegerField(verbose_name="#")
    title_section = models.CharField(max_length = 100, verbose_name="заголовок")
    #markdown_content = models.TextField(verbose_name="содержание", 
    #editable = False)
    html_content = models.TextField(verbose_name="") #, editable = False)
    file_to=models.FileField(verbose_name = "файл", blank = True, 
    upload_to="wiki/article", default = '')
    def __str__(self):
        return self.title_section
    class Meta:
        verbose_name='содержание секции'
        verbose_name_plural='содержание секции'
        ordering=['ordnum'] 
        unique_together = ['article','ordnum']

