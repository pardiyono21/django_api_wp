from django.shortcuts import render, get_object_or_404
from .api import get_articles, get_article_detail

def article_list(request):
    articles = get_articles()
    return render(request, 'artikel/artikel_list.html', {'articles': articles})

def article_detail(request, slug):
    article = get_article_detail(slug)
    if article is None:
        return render(request, 'artikel/artikel_not_found.html')  # Halaman error jika artikel tidak ditemukan
    return render(request, 'artikel/artikel_detail.html', {'article': article})
