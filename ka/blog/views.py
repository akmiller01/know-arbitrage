import math
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from django.contrib import messages
from blog.models import Post
from blog.models import Tag
from blog.models import Stock
from blog.models import Page
from blog.models import Comment
from blog.forms import CommentForm
from blog.utils import *
from ipware.ip import get_ip

def index(request):
    #Filter by tags and queries
    queryParam = request.GET.get('q')
    tagParam = request.GET.get('tag')
    if tagParam:
        post_list = Post.objects.filter(published=True, tag__slug=tagParam)
    elif queryParam:
        postQuery = get_query(queryParam, ['title', 'content','description','tag__name','stock__symbol','stock__company'])
        post_list = Post.objects.filter(postQuery,published=True).distinct()
    else:
        post_list = Post.objects.filter(published=True)
    paginator = Paginator(post_list,3) # Show 3 posts per page
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
    #find all published pages
    pages = Page.objects.filter(published=True)
    #now return the rendered template
    return render(request,'blog/index.html',{'posts':posts,'tags':tags,'half_tags':half_tags,'tagParam':tagParam,'queryParam':queryParam,'stockLen':stockLen,'pages':pages})

def post(request,slug):
    #get the Post object
    post = get_object_or_404(Post,slug=slug)
    #Tags
    tags = Tag.objects.filter(post__slug=post.slug)
    half_tags = math.ceil(len(tags)/2.0)
    #Stocks
    post.stocks = Stock.objects.filter(post__slug=post.slug)
    stockLen = len(post.stocks)
    #Comments
    comments = Comment.objects.filter(post=post,validated=True)
    #find all published pages
    pages = Page.objects.filter(published=True)
    #now return the rendered template
    return render(request,'blog/post.html',{'post':post,'tags':tags,'half_tags':half_tags,'stockLen':stockLen,'pages':pages,'comments':comments,'form':CommentForm()})

def page(request,slug):
    page = get_object_or_404(Page,slug=slug)
    #find all published pages
    pages = Page.objects.filter(published=True)
    #Tags
    tags = Tag.objects.all()
    half_tags = math.ceil(len(tags)/2.0)
    return render(request,'blog/page.html',{'page':page,'pages':pages,'tags':tags,'half_tags':half_tags,'pages':pages})

def add_comment(request, slug):
    """Add a new comment."""
    p = request.POST
    post = Post.objects.get(slug=slug)
    author_ip = get_ip(request)

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=post)
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.author_ip = author_ip
        comment.save()
        messages.success(request,'Thank you for submitting a comment. It will appear once reviewed by an administrator.')
    else:
        messages.error(request, 'Something went wrong. Please try again later.')
    return HttpResponseRedirect(post.get_absolute_url())
