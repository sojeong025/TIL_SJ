from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'num' : 30
    }
    return render(request, "articles/index.html", context)


# Create your views here.
