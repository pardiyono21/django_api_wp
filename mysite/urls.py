

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('fetch-wordpress-data/', views.fetch_wordpress_data, name='fetch_wordpress_data'),
    path('artikel/', include('artikel.urls')),
    path('project/', include('project.urls')),
    path('tags/', include('tags.urls')),
    path('admin/', admin.site.urls),
]
