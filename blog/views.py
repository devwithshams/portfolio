from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    posts = Blog.objects.order_by('-date')[:6]
    
    return render(request, 'blog/all_blogs.html', {'posts': posts})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})