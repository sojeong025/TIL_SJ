from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # 모든 게시글 보여줘
    articles = Article.objects.all()
    # for article in articles:
    #     print(article.pk)
    #     print(article.title)
    #     print(article.content)
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # print(dir(request))
    print('='*30)
    print(request.GET)
    print('='*30)

    title = request.GET.get('title')
    content = request.GET.get('content')

    print(title, content)
    
    # ORM
    # class.manager.queryAPI
    # Article.objects.create()


    # 1. article instance 생성하는 방법 (더 많이 사용) 
    article = Article()
    article.title = title
    article.content = content
    print(article.title)
    print(article.content)
    # 아직 db에 반영된 것은 아님
    print(article.pk)
    # db에 위의 내용을 반영하는 방법은?
    article.save()
    print('db에 저장 후')
    print(article.pk)


    # 2. 두번째 방법 Class.Manager.Query API
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')