from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    # ORM
    # class.manager.query API
    # 함수의 실행 결과를 변수에 담는다.
    articles = Article.objects.all()
    context = {
        # 특정 단어 혹은 알파벳을 영역 선택 후
        # ctrl + d 하면 같은 단어 다 찾아줌
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    # 특정 게시글 하나 조회
    # class.manager.query API
    # 함수 실행 -> article_pk와 pk값이 동일한 게시글 하나 조회
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 게시글 생성 요청에 대한 응답이므로
    # 게시글 생성만 해주면 되는 것이 이 view 함수의 일이다
    # 진짜 게시글만 만들어주면 UX 가 박살남
    # 게시글 생성 후에, 특정 페이지를 사용자에게 반환 할 수 있도록
    
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    # 다른 요청 경로로 이동시킨다
    return redirect('articles:detail', article.pk)

def edit(request, article_pk):
    # class.manage.query API
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')