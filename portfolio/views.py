from django.shortcuts import render
from .models import Project

def home(request):
    objects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'objects':objects})


# Create your views here.
