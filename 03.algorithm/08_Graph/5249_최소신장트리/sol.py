import sys
sys.stdin = open('input.txt')

# x가 속한 집단의 대표 리턴
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

# y의 대표원소가 x의 대표원소를 가리키도록
def union(x, y):
    parent[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):

    # 0~V 정점 번호 | E 간선 수
    V, E = map(int, input().split())

    # makeset()
    parent = [i for i in range(V+1)]
    graph = []
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        graph.append([v1, v2, w])


    # (1) 가중치 기준 오름차순 정렬
    graph.sort(key=lambda x:x[2])

    # (2) N개 정점(V+1), N-1개의 간선 선택
    N = V + 1
    s = 0
    cnt = 0
    for u, v, w in graph:
        if find_set(u) != find_set(v):
            cnt += 1
            s += w
            union(u, v)
            if cnt == N-1:
                break
    print(f'#{tc} {s}')
