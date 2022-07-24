from django.forms import ModelForm
from django import forms

from core.models import Phone

class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = 'mark', 'model', 'picture'