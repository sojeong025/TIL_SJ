# 최소생산비용 (주석달기 귀찮)
import sys
sys.stdin = open('input.txt')


def backtracking(i, tmp):
    global cost
    if i == N:
        cost = min(tmp, cost)
        return
    if tmp >= cost:
        return
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                backtracking(i+1, tmp + arr[i][j])
                visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]    # 열만 체크하면 됨
    cost = 100 * N

    backtracking(0, 0)
    print(f'#{tc} {cost}')

