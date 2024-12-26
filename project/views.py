from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404
from .api import get_projects, get_project_detail
import random
from django.core.cache import cache
import hashlib


def project_list(request):
    cache_key = 'project_list_cache'
    cached_data = cache.get(cache_key)

    # Ambil data dari API WordPress
    projects = get_projects()
    current_hash = hashlib.md5(str(projects).encode('utf-8')).hexdigest()

    # Jika data cache ada dan sama dengan hash terbaru, gunakan cache
    if cached_data and cached_data.get('hash') == current_hash:
        projects = cached_data['data']
    else:
        # Simpan data baru ke cache
        cache.set(cache_key, {'hash': current_hash, 'data': projects}, 60 * 15)

    return render(request, 'project/project_list.html', {'projects': projects})


# Gunakan cache_page untuk menyimpan hasil render halaman selama 15 menit
@cache_page(60 * 15)  # Cache selama 15 menit
def project_detail(request, slug):
    project = get_project_detail(slug)

    # Daftar kelas untuk tag
    classes = ['bg-primary', 'bg-secondary', 'bg-success', 'bg-danger']

    # Pilih kelas acak untuk setiap tag
    tags_with_classes = [
        {
            'name': tag['name'],
            'class': random.choice(classes)
        }
        for tag in project.get('tags_details', [])
    ]

    if project is None:
        return render(request, 'project/project_not_found.html')  # Halaman error jika project tidak ditemukan
    return render(request, 'project/project_detail.html', {'project': project,'tags_with_classes': tags_with_classes})
