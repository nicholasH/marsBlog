from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Blog , Gallery

def blog(request):

    post_gall_dict = dict()
    posts = Blog.objects.all()

    postlist = []

    for p in posts:
        g = Gallery.objects.filter(post=p)
        postlist.append([p,list(g)])





    return render(request, 'blog/blog.html', {"postlist":reversed(postlist)})