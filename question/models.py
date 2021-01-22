from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class About(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_about')
    contents = models.TextField(verbose_name='문의사항')
    create_date = models.DateTimeField(verbose_name='등록시간')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='수정시간')

    def __str__(self):
        return str(self.contents) + ', ' + str(self.author)

    class Meta:
        db_table = '문의사항'
        verbose_name = '문의사항'
        verbose_name_plural = '문의사항'