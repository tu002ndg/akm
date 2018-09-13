from django.conf.urls import url
from akm.wiki.models import Article
from django.views.generic.list import ListView
#from akm.wiki.views import ArticleList
from akm.wiki import views

urlpatterns = [
    url(r'^$', views.index, name = "wiki"),
    url(r'^article/part/(?P<slug>[-\w]+)$',views.articles, 
    name = "wiki_part_article"),
    url(r'^article/(?P<pk>\d+)/detail/$', 
    ListView.as_view(),
    {
        'queryset': Article.objects.all(),
    },
    name='wiki_article_detail'),
#    url(r'^history/(?P<slug>[-\w]+)$',
#        'wiki.views.article_history',
#        name='wiki_article_history'),
#    url(r'^add/article$',
#        'wiki.views.add_article',
#        name='wiki_article_add'),
#    url(r'^edit/article/(?P<slug>[-\w]+)$',
#        'wiki.views.edit_article',
#        name='wiki_article_edit'),
]

