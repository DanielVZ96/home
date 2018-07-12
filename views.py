from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'home/home.html', context={'projects':projects})

def contact(request):
    pass