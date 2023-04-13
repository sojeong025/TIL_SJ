from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Music
from .serializers import MusicSerializer

# Create your views here.
@api_view(['GET'])
def music_list(request):
    # 모든 음악 리스트를 응답(JSON 형식으로)
    musics = Music.objects.all()    # 1. DB에서 데이터를 가져온다.
    serializer = MusicSerializer(musics, many=True)   # 2. 가져온 데이터를 담는다
    # QuerySet 으로 리턴되는 경우
    # 조회되는 데이터가 0개 이상인 경우 (many 설정 필수)
    # all(), filter()
    # 객체로 리턴되는 경우
    # .get() 한개만 무조건 리턴하기 때문에 QuerySet에 담을 필요 없음
    # many 설정 필요없음
    # 3. 작성된 시리얼라이져의 데이터를 응답으로 리턴한다.
    return Response(serializer.data)

def music_detail(request, music_pk):
    music = Music.objects.get(pk=music_pk)
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializer(music)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def music_list_create(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



