from django.db import models

# Create your models here.

class User(models.Model):

    objects = models.Manager()

    username = models.CharField(max_length=32, verbose_name='아이디')
    nickname = models.CharField(max_length=32, verbose_name='닉네임')
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return str(self.username) + ' ' + str(self.nickname)

    class Meta:
        db_table = '사용자'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'