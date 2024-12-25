from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.tag_articles, name='tag_articles'),
    path('', views.tag_list, name='tag_list'),  # Tambahkan URL ini jika 'tag_list' diperlukan
]
