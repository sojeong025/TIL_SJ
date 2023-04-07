from django.shortcuts import render, redirect
from .models import Post
from django import forms
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' :posts,
    }
    return render(request, 'posts/index.html', context)


def create(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'posts/create.html', context)

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')