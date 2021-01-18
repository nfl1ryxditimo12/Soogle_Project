from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    objects = models.Manager()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')
    title = models.CharField(max_length=64, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    create_date = models.DateTimeField(verbose_name='등록시간')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='수정시간')

    voter = models.ManyToManyField(User, related_name='voter_post')

    def __str__(self):
        return self.title

    class Meta:
        db_table = '글'
        verbose_name = '글'
        verbose_name_plural = '글'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    contents = models.TextField(verbose_name='내용')
    create_date = models.DateTimeField(verbose_name='등록시간')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='수정시간')
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.contents

    class Meta:
        db_table = '댓글'
        verbose_name = '댓글'
        verbose_name_plural = '댓글'