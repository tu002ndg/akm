from django import forms
from akm.wiki.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author', 'slug']
    
    def get_queryset(self):
        return Article.objects.all()