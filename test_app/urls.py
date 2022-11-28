from django.urls import re_path, path
from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.post_detail, name='post'),
    path('post_new', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list')
]
