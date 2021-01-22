from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('', views.about, name='about'),
    path('write/', views.question_write, name='question_write'),
    path('delete/<int:question_id>/', views.question_delete, name='question_delete'),
]