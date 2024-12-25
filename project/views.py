from django.shortcuts import render, get_object_or_404
from .api import get_projects, get_project_detail

def project_list(request):
    projects = get_projects()
    return render(request, 'project/project_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_project_detail(slug)
    if project is None:
        return render(request, 'project/project_not_found.html')  # Halaman error jika project tidak ditemukan
    return render(request, 'project/project_detail.html', {'project': project})
