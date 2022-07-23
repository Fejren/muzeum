from django.forms import ModelForm
from django import forms
from tinymce.widgets import TinyMCE
from .models import *


class MessageForm(ModelForm):
    check = forms.BooleanField(required=True)
    email = forms.EmailField()

    class Meta:
        model = Message
        fields = 'name', 'email', 'title', 'message', 'check'


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = 'mark', 'model', 'picture'


class ArticleForm(ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 15}))

    class Meta:
        model = Article
        fields = 'title', 'body', 'picture', 'status', 'author'
