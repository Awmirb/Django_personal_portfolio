from django.shortcuts import render, get_object_or_404
from .models import blogs
# Create your views here.

def all_blogs(request):
    blog_count = blogs.objects.all().count
    all_blogs = blogs.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':all_blogs, 'blog_count':blog_count})

def detail(request, blog_id):
    blog_page = get_object_or_404(blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog_page':blog_page})
