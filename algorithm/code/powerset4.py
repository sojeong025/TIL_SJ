# 순열1 .......

def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(i, k):   # 갈림길이 여러 개일 때
                                # 왼쪽이랑 교환안하기 위해 i,k로 진행
            p[i], p[j] = p[j], p[i]
            # p[i] 결정, p[i]와 관련된 작업 가능
            f(i+1, k)   # 다음 자리를 결정하러
            p[i], p[j] = p[j], p[i]

p = [1, 2, 3]
N = len(p)
f(0, N)
