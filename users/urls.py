from django.urls import re_path, path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(),name='signup')
]
