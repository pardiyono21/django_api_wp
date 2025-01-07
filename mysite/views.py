from django.views.decorators.cache import cache_page
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
import requests

# Gunakan cache_page untuk menyimpan hasil render halaman selama 15 menit
#@cache_page(60 * 15)  # Cache selama 15 menit
def index(request):
    # API URL untuk kategori 70
    wordpress_api_url_70 = "https://pardi.jambishow.com/wp-json/wp/v2/posts?categories=70&per_page=4"
    # API URL untuk kategori 69
    wordpress_api_url_69 = "https://pardi.jambishow.com/wp-json/wp/v2/posts?categories=69&per_page=4"

    # Mengambil data dari API kategori 70
    response_70 = requests.get(wordpress_api_url_70)
    posts_data_70 = []
    if response_70.status_code == 200:
        posts_data_70 = response_70.json()
        for post in posts_data_70:
            post_date = post['date']
            # Mengonversi string tanggal ke objek datetime
            post_datetime = datetime.strptime(post_date, "%Y-%m-%dT%H:%M:%S")
            
            # Format tanggal: Hari, Tanggal Bulan Tahun
            post['formatted_date'] = post_datetime.strftime("%A, %d %B %Y")
    
    # Mengambil data dari API kategori 69
    response_69 = requests.get(wordpress_api_url_69)
    posts_data_69 = []
    if response_69.status_code == 200:
        posts_data_69 = response_69.json()
        for post in posts_data_69:
            post_date = post['date']
            # Mengonversi string tanggal ke objek datetime
            post_datetime = datetime.strptime(post_date, "%Y-%m-%dT%H:%M:%S")
            
            # Format tanggal: Hari, Tanggal Bulan Tahun
            post['formatted_date'] = post_datetime.strftime("%A, %d %B %Y")

    # Menggabungkan kedua data posts
    context = {
        'title': 'Devendlin',
        'description': 'Full-Stack Developer and Linux Enthusiast',
        'posts_70': posts_data_70,  # Data kategori 70
        'posts_69': posts_data_69,  # Data kategori 69
    }

    # Mengembalikan data ke template
    return render(request, 'home.html', context)
    #return render(request,"home.html", context)

# Gunakan cache_page untuk menyimpan hasil render halaman selama 15 menit
@cache_page(60 * 15)  # Cache selama 15 menit
def fetch_wordpress_data(request):
    wordpress_api_url = "https://pardi.jambishow.com/wp-json/wp/v2/posts?categories=70&per_page=4"
    
    # Mengambil data menggunakan requests
    response = requests.get(wordpress_api_url)
    
    if response.status_code == 200:
        # Mengambil data JSON dari API
        posts_data = response.json()
        
        # Mengembalikan data ke template atau dalam bentuk JSON
        return JsonResponse(posts_data, safe=False)
    else:
        return JsonResponse({"error": "Failed to retrieve data from WordPress API"}, status=500)