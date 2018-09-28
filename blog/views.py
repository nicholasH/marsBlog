from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Blog , Gallery

def blog(request):

    post_gall_dict = dict()
    posts = Blog.objects.all()


    for p in posts:
        post_gall_dict[p] = Gallery.objects.get(post = p)

    picList = list(Gallery.objects.all())

    print(post_gall_dict)



    return render(request, 'blog/blog.html', {'blogs': posts,"dict":post_gall_dict})