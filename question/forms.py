from django import forms
from .models import About

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['contents']
        labels = {
            'contents': '문의사항',
        }