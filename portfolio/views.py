from django.shortcuts import render, get_object_or_404
from .models import Project


def homePage(request):
    projects = Project.objects.all()[:2]
    return render(request, 'portfolio/home.html', {'projects': projects})

def resume(request):
    return render(request, 'portfolio/resume.html')

def contact(request):
    return render(request, 'portfolio/contacts.html')

def ListView(request):
    lists = Project.objects.all()

    return render(request, 'portfolio/lists.html', {'lists': lists})

