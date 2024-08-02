from django import forms
from .models import TextModel

class TextForm(forms.ModelForm):
    class Meta:
        model = TextModel
        fields = ['text']
