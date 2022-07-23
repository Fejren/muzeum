from django.forms import ModelForm
from django import forms

from tinymce.widgets import TinyMCE

class ArticleForm(ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 15}))