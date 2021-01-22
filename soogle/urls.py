from django.urls import path
from . import views

app_name = 'soogle'

urlpatterns = [
    path('write/', views.post_write, name='post_write'),
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('comment/write/<int:post_id>/', views.comment_write, name='comment_write'),
    path('vote/<int:post_id>/', views.post_vote, name='post_vote'),
    path('membership/', views.soogle_membership, name='soogle_membership'),

]