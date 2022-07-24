from django.forms import ModelForm
from django import forms

from tinymce.widgets import TinyMCE

from core.models import Article


class ArticleForm(ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 15}))

    class Meta:
        model = Article
        fields = 'title', 'body', 'picture', 'status', 'author'
