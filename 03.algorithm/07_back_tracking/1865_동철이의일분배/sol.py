# 동철이의 일분배
import sys
sys.stdin = open('input.txt')


# i = i번째 사람 | tmp = 확률 계산해가는 거
def backtracking(i, tmp):
    global max_per
    if tmp <= max_per:
        return
    # 모든 직원이 일을 마쳤을 때 값 비교
    if i == N:
        max_per = max(max_per, tmp)
        return

    for j in range(N):
        # 일이 선택되지 않았다면
        if not visited[j]:
            visited[j] = 1
            backtracking(i+1, tmp * (arr[i][j] * 0.01))
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # 0이 최대로 작기 때문에 비교할 최대 확률(이래서 max로 뒀던..)
    max_per = 0

    # 확률은 1에서부터 낮아지기
    backtracking(0, 1)
    answer = format(max_per*100, '.6f')

    print(f'#{tc} {answer}')

