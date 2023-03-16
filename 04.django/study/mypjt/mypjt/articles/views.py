from django.shortcuts import render

# Create your views here.

def hello(request, name):
    context = {
        'name' : name
    }
    return render(request, 'articles/hello.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'articles/catch.html', context)
