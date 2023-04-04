# # disjoint set

# def find_set(x):    # x가 속한 집합의 대표 리턴
#     while x != rep[x] :     # x==rep[x]까지
#         x = rep[x]
#     return x

 
# def union(x,y):     # y의 대표원소가 x의 대표원소를 가리키도록
#     rep[find_set(y)] = find_set(x)
#     # rep[y] = find_set(x)로 하면 안되는거 주의


# # makeset()
# rep = [i for i in range(6)]
# print(rep)

import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())    # 0~ V 정점번호, E 간선 수


def find_set(x):    
    while x != rep[x] :     
        x = rep[x]
    return x

 
def union(x,y):    
    rep[find_set(y)] = find_set(x)

# makeset()
rep = [i for i in range(V+1)]
graph = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph.append([v1, v2, w])

# (1) 가중치 기준 오름차순 정렬
graph.sort(key=lambda x:x[2])

# (2) N개 정점(V+1), N-1개의 간선 선택
N = V + 1
s = 0   # MST에 포함된 간선의 가중치 합
cnt = 0
MST = []
# 가중치가 작은 것부터.. (앞에서부터 순서대로)
for u, v, w in graph:
    if find_set(u) != find_set(v):  # 사이틀이 생기지 않으면
        cnt += 1
        s += w  # 가중치 합
        MST.append([u,s,v])
        union(u, v)
        if cnt == N-1:  # MST 구성 완료
            break
print(MST)
print(s)


