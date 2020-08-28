from django.shortcuts import render,redirect
from .models import *
import markdown
from django.contrib import messages
from django.db.models import Q
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
import re

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request,'index.html',locals())

# 文章详情页
def detail(request,pk):
    post = Post.objects.get(pk=pk)
    # 阅读量 +1
    post.increase_views()

    post.body = markdown.markdown(post.body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        #在顶部引入 TocExtension 和 slugify
        TocExtension(slugify=slugify),
    ])

    return render(request,'detail.html',locals())

# 文章分类
def category(request,pk):
    category = Category.objects.get(pk=pk)
    post_list = Post.objects.filter(category=category).order_by('-create_time')
    return render(request,'index.html',locals())

# 文章时间轴
def archive(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request,'archive.html',locals())

def about(request):
    return render(request,'about.html',locals())

# 搜索功能
def search(request):
    q = request.GET.get('q')
    if not q:
        error_msg = '请输入搜索关键词'
        messages.add_message(request,messages.ERROR,error_msg,extra_tags='danger')
        return redirect('index')
    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request,'index.html',locals())