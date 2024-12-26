from django.views.decorators.cache import cache_page
import random
from django.shortcuts import render
from .api import get_articles, get_article_detail

# Gunakan cache_page untuk menyimpan hasil render halaman selama 15 menit
#@cache_page(60 * 15)  # Cache selama 15 menit
def article_list(request):
    articles = get_articles()
    return render(request, 'artikel/artikel_list.html', {'articles': articles})

# Gunakan cache_page untuk menyimpan hasil render halaman selama 15 menit
@cache_page(60 * 15)  # Cache selama 15 menit
def article_detail(request, slug):
    article = get_article_detail(slug)
    # Daftar kelas untuk tag
    classes = ['bg-primary', 'bg-secondary', 'bg-success', 'bg-danger']

    # Pilih kelas acak untuk setiap tag
    tags_with_classes = [
        {
            'name': tag['name'],
            'class': random.choice(classes)
        }
        for tag in article.get('tags_details', [])
    ]

    if article is None:
        return render(request, 'artikel/artikel_not_found.html')  # Halaman error jika artikel tidak ditemukan
    return render(request, 'artikel/artikel_detail.html', {'article': article, 'tags_with_classes': tags_with_classes})
