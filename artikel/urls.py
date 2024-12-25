from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('detail/<slug>/', views.article_detail, name='article_detail'),
]