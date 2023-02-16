# def f(i, k, s, t):   # i원소. k집합의 크기, s i-1까지 고려된 합, t 목표
#     global cnt
#     if i == k:
#         if s == t:
#             cnt += 1
#         return
#     else:
#         f(i+1, k, s+A[i], t)    # A[i] 포함
#         f(i+1, k, s, t)         # A[i] 미포함
#
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(A)
# key = 10
# cnt = 0
# bit = [0] * N
#
# f(0, N, 0, key)
# print(cnt)          # 합이 key인 부분집합의 수

def f(i, k, s, t):   # i원소. k집합의 크기, s i-1까지 고려된 합, t 목표
    global cnt
    global fcnt
    fcnt += 1
    if i == k:
        if s == t:
            cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)    # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)         # A[i] 미포함


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


N = len(A)
key = 10
cnt = 0
bit = [0] * N
fcnt = 0    # 함수 호출 횟수
f(0, N, 0, key)
print(cnt, fcnt)          # 합이 key인 부분집합의 수
