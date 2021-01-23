from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ['title', 'contents']
        labels = {
            'title': '제목',
            'contents': '내용,'
        }