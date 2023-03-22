from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

# login 이라는 행위는 결국 session을 '생성'하는 행위
# GET 요청이 우선이 되어야 한다 -> POST 요청을 보낼 수 있는 페이지가 필요하므로,
# POST 요청
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            # session id 생성
            login()
        # 인증 절차를 위한 form 태그
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

