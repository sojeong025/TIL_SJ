dust=int(input())

if dust <=30 :
    print("좋음")
elif dust <=80 :
    print("보통")
elif dust <=150 :
    print("나쁨")
else :
    print("매우나쁨")
print("미세먼지 확인 완료")


d=int(input())

if d > 150 :
    print("매우나쁨")
    if d>300:
        print("실외 활동을 자제하세요.")
elif d>80 :
    print("나쁨")
elif d>30 :
    print("보통")
elif d >=0 :
    print("좋음")
else:
    print("실외 활동을 자제하세요")
print("미세먼지 확인 완료")