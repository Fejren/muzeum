from django import http
from django.forms import ModelForm
from django import forms

from core.models import Message


class MessageForm(ModelForm):
    check = forms.BooleanField(required=True)
    email = forms.EmailField()

    class Meta:
        model = Message
        fields = 'name', 'email', 'title', 'message', 'check'
