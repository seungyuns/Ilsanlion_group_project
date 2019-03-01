from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request, 'home.html')

def show(request):
    blogs=Blog.objects
    return render(request,'show.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'detail':blog_detail})

def new(request):
    return render(request,'new.html')   

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/detail/'+str(blog.id))

def destroy(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    blog.delete()
    return redirect('/blog/show/')

