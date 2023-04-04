import sys
sys.stdin = open('input.txt')

def dijkstra(s, V):     # s 출발, V 마지막 정점 번호
    U = [0] * (V+1)
    U[s] = 1
    for i in range(V+1):
        D[i] = adjM[s][i]

    N = V + 1
    for _ in range(N-1):
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                w = i
                minV = D[i]
        U[w] = 1
        for v in range(V+1):
            if 0 < adjM[w][v] < INF:
                D[v] = min(D[v], D[w] + adjM[w][v])

T = int(input())
for tc in range(1, T+1):
    INF = 10000
    # 0~N번 정점, E 간선 수
    N, E = map(int, input().split())
    adjM = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        adjM[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w


    D = [0] * (N+1)
    dijkstra(0, N)
    print(f'#{tc} {D[-1]}')

