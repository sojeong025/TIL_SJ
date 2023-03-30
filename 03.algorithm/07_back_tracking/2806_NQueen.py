import sys
sys.stdin = open('input.txt')


def check(i, j):
    for di, dj in [[-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i+di, j+dj
        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj]:   # 다른 퀸이 있으면
                return 0        # 실패
            ni, nj = ni+di, nj+dj
    return 1        # i, j에 퀸을 놓을 수 있음


def backtracking(i, N):
    global cnt
    if i == N:  # N개의 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            if check(i, j):
                board[i][j] = 1
                # 다음 열로 돌아가서 다시 0으로 설정해 백트래킹
                backtracking(i+1, N)
                board[i][j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 말을 뒀는지 체크하는 보드
    board = [[0]*N for _ in range(N)]
    cnt = 0
    backtracking(0, N)
    print(f'#{tc} {cnt}')