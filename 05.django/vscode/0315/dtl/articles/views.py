from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    return render(request, 'articles/create.html')

# name을 url로 부터 받아와서 사용
# path가 profile 호출할 때, name=name으로 호출
# 그러면 함수도 정의 되어야 함
def profile(request, name):
    # print('='*30)
    # print(name)
    # print('='*30)
    # context 이름은 관념적인 것 .. django가 기본 구조 짤 때 그렇게 이름 지었음
    # 꼭 이 이름일 필요는 없는데, 굳이 다른 이름으로 지을 이유도 없음
    context = {
        #key:value
        'name':name
    }
    return render(request, 'articles/profile.html',context)

def info(request, age):
    context = {
        'age' : age
    }
    return render(request, 'articles/info.html', context)
