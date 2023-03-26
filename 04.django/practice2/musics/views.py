from django.shortcuts import render, redirect
from .models import Music
from django import forms
from .forms import MusicForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
    musics = Music.objects.all()
    context = {
        'musics' : musics,
    }
    return render(request, 'musics/index.html', context)

@require_safe
def detail(request, pk):
    music = Music.objects.get(pk=pk)
    context = {
        'music' : music
    }
    return render(request, 'musics/detail.html', context)

def create(request):
    if request.method=='POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save()
            return redirect('musics:detail', music.pk)
    else:
        form = MusicForm()

    context = {'form':form}
    return render(request, 'musics/create.html',context)

def update(request, pk):
    music = Music.objects.get(pk=pk)
    if request.method =="POST":
        form = MusicForm(request.POST, request.FILES, instance=music)
        if form.is_valid():
            music.save()
            return redirect('musics:detail', pk=music.pk)
    else:
        form = MusicForm(instance=music)
    context = {'form':form, 'music':music}
    return render(request, 'musics/update.html', context)

@require_POST
def delete(request, pk):
    music = Music.objects.get(pk=pk)
    music.delete()
    return redirect('musics:index')