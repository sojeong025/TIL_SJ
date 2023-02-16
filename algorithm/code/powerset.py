# 
# def f(i, k):
#     if i == k:
#         print(bit)
#     else:
#         bit[i] = 1
#         f(i+1, k)
#         bit[i] = 0
#         f(i+1, k)


# # 부분집합의 원소 출력
# def f(i, k):
#     if i == k:
#         for j in range(k):
#             if bit[j]:
#                 print(A[j], end = ' ')
#         # print()
#         print(bit)
#     else:
#         bit[i] = 1
#         f(i+1, k)
#         bit[i] = 0
#         f(i+1, k)
#
# A = [1, 2, 3]
# N = len(A)
# bit = [0]*N
# f(0,N)


# # 부분집합의 합 구하기
# def f(i, k):
#     if i == k:  # 하나의 부분집합 완성
#         s = 0
#         for j in range(k):
#             if bit[j]:
#                 s += A[j]  # 부분집합의 합
#         print(bit, s)
#
#     else:
#         bit[i] = 1
#         f(i + 1, k)
#         bit[i] = 0
#         f(i + 1, k)
#
#
# A = [1, 2, 3]
# N = len(A)
# bit = [0] * N
# f(0, N)

# # 원소의 합이 10인 경우가 있니?
# def f(i, k, key):
#     if i == k:  # 하나의 부분집합 완성
#         s = 0
#         for j in range(k):
#             if bit[j]:
#                 s += A[j]  # 부분집합의 합
#         if s == key:
#             return 1
#         else:
#             return 0
#         # if s == key:    # 합이 key와 같은 부분집합을 출력
#         #     for j in range(k):
#         #         if bit[j]:
#         #             print(A[j], end=' ')
#         #     print()
#
#     else:
#         bit[i] = 1
#         f(i + 1, k, key)
#         bit[i] = 0
#         f(i + 1, k, key)
#
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(A)
# bit = [0] * N
# f(0, N, 10)
