from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Blog

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blog})