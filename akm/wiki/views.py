from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from akm.wiki.models import Part

maps =[
    {"url":'main', "name":'Главная'},
    {"url":'wiki', "name":'Wiki'},
    ]

@login_required
def index(request):
    parts = Part.objects.all()
    return render(request,'wiki.html',{"wiki_parts":parts,
    "akm_maps":maps})

@login_required
def articles(request, slug):
    return render(request,'articles.html',{"wiki_part":slug,
    "akm_maps":maps})


#class ArticleList(ListView):
#    model = Article
