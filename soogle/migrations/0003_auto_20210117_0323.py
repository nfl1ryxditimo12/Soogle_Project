# Generated by Django 3.1.5 on 2021-01-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soogle', '0002_auto_20210117_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='수정시간'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='수정시간'),
        ),
    ]
