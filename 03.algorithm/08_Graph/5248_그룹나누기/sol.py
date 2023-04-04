import sys
sys.stdin = open('input.txt')

# 자신이 속한 집단의 대표원소 (parent의 값)
def find_set(x):
    # while x != parent[x]:
    #     x = parent[x]
    # return x

    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])


def union(x, y):
    # parent[y의 부모] = x의 부모
    # parent[find_set(y)] = find_set(x)
    # print(parent, x, y)

    x = find_set(x)
    y = find_set(y)

    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y

    if rank[x] == rank[y]:
        rank[x] += 1


T = int(input())
for tc in range(1, T+1):
    # N=전체 사람 번호  M=제출된 쪽지의 수
    N, M = map(int, input().split())
    # 간선 정보
    edge = list(map(int, input().split()))
    # print(edge)

    # make_set
    parent = list(range(N+1))
    rank = [0] * (N+1)
    # print(parent)
    # print()

    for i in range(M):
        x = edge[i*2]
        y = edge[i*2+1]
        union(x, y)
    # parent = set(parent)
    result = set()
    for i in range(1, N+1):
        result.add(find_set(i))
    print(f'#{tc} {len(result)}')