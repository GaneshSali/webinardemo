from django.shortcuts import render, redirect
from .models import Blog


def index(request):
    blogs = Blog.objects.all().order_by('-id')
    return render(request,'myapp/index.html',{'blogs':blogs})


def create(request):
    
    if request.method == "POST":
        
        title = request.POST['title']
        desc = request.POST['desc']
        Blog.objects.create(title=title,desc=desc)
        return redirect('index',{'dd':"ff"})
    else:
        return render(request,'myapp/create.html')


def edit(request,id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        blog.title = title
        blog.desc = desc
        blog.save()
        return redirect('index')
    else:
        return render(request,'myapp/edit.html',{'blog': blog})


def delete(request,id):

    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('index')
