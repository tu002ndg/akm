from django.shortcuts import render
#from django.template import loader
#from django.template import Context
from akm.wiki.models import Article

# Create your views here.
def search(request):
    query = request.GET.get('q','')
    results = []
    if (query):
        results = Article.objects.filter(title__icontains=query)|Article.objects.filter(abstract__icontains=query)
    #template = loader.get_template('search.html')
    template_name = 'search.html'
    context = {'query':query, 'results':results}
    return render(request, template_name, context)