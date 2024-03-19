from django.urls import path, include
from . import views

app_name = 'kristina'

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag'),
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
    path('author_info/<int:id>/', views.author_info, name='author_info'),
    path('<int:page>', views.main, name='root_paginate')

]
