from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('', views.notice_list, name="notice_list"),
    path('write/', views.notice_write, name='notice_write'),
    path('<int:notice_id>/', views.notice_detail, name='notice_detail'),
    path('delete/<int:notice_id>/', views.notice_delete, name='notice_delete'),
    path('modify/<int:notice_id>/', views.notice_modify, name='notice_modify'),
    path('vote/<int:notice_id>/', views.notice_vote, name='notice_vote'),
]