from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents']
        labels = {
            'title': '제목',
            'contents': '내용,'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['contents']
        labels = {
            'contents': '답변내용',
        }
