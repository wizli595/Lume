from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'content','hidden']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }
