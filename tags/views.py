import requests
from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Gunakan cache_page untuk menyimpan hasil render halaman selama 15 menit
@cache_page(60 * 15)  # Cache selama 15 menit
def tag_list(request):
    return render(request, 'tags/tags_list.html')

# Gunakan cache_page untuk menyimpan hasil render halaman selama 15 menit
@cache_page(60 * 15)  # Cache selama 15 menit
def tag_articles(request, slug):
    # URL API WordPress untuk mendapatkan tag ID berdasarkan slug
    tag_url = f"https://appscenter.site/wp-json/wp/v2/tags?slug={slug}"
    
    try:
        # Fetch tag ID
        tag_response = requests.get(tag_url)
        tag_response.raise_for_status()
        tag_data = tag_response.json()
        
        if tag_data:
            tag_id = tag_data[0]['id']  # Ambil ID dari response pertama
            
            # URL API untuk mendapatkan artikel berdasarkan tag ID
            posts_url = f"https://appscenter.site/wp-json/wp/v2/posts?tags={tag_id}"
            posts_response = requests.get(posts_url)
            posts_response.raise_for_status()
            posts = posts_response.json()
        else:
            posts = []
    except requests.exceptions.RequestException as e:
        posts = []
        print(f"Error fetching data: {e}")
    
    # Render template dengan daftar artikel
    return render(request, 'tags/tag_articles.html', {'posts': posts, 'slug': slug})
