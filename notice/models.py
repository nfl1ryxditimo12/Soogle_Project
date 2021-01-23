from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notice(models.Model):

    objects = models.Manager()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notice_author')
    title = models.CharField(max_length=64, verbose_name='공지사항')
    contents = models.TextField(verbose_name='공지내용')
    create_date = models.DateTimeField(verbose_name='등록일')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='수정시간')

    voter = models.ManyToManyField(User, related_name='notice_voter')

    def __str__(self):
        return str(self.title) + ' - ' + str(self.create_date)

    class Meta:
        db_table = '공지사항'
        verbose_name = '공지사항'
        verbose_name_plural = '공지사항'