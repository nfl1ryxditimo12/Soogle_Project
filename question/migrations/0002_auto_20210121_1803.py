# Generated by Django 3.1.5 on 2021-01-21 09:03

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='about',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
