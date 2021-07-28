from django.shortcuts import render

from .models import Project

# Create your views here.

projects = Project.objects.all()

def index(request):
    return render(request, 'portfolio/index.html', context={'projects': projects})