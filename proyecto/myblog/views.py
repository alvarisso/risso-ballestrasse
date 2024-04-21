from django.shortcuts import render

# Create your views here.

# En el archivo myblog/views.py
from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'myblog/home.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'myblog/post_detail.html', {'post': post})
