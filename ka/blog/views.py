import math
from itertools import chain
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post
from blog.models import Tag
from blog.models import Stock
from blog.models import About

def index(request):
    #get the blog posts that are published
    tagParam = request.GET.get('tag')
    if tagParam:
        post_list = Post.objects.filter(published=True, tag__slug=tagParam)
    else:
        post_list = Post.objects.filter(published=True)
    paginator = Paginator(post_list,4) # Show 4 posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        #If page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)
    #Tags
    tags = Tag.objects.all()
    half_tags = math.ceil(len(tags)/2.0)
    #Relevant stocks
    stockLen = 0
    for post in posts:
            post.stocks = Stock.objects.filter(post__slug=post.slug)
            stockLen += len(post.stocks)
    #now return the rendered template
    return render(request,'blog/index.html',{'posts':posts,'tags':tags,'half_tags':half_tags,'tagParam':tagParam,'stockLen':stockLen})

def about(request):
    about = About.objects.all()[:1].get()
    return render(request,'blog/about.html',{'about':about})

def post(request,slug):
    #get the Post object
    post = get_object_or_404(Post,slug=slug)
    post.tags = Tag.objects.filter(post__slug=post.slug)
    #now return the rendered template
    return render(request,'blog/post.html',{'post':post})
