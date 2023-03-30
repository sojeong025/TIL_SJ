import sys
sys.stdin = open('input.txt')


# i = 정류장 위치 | tmp = 충전 횟수
def backtracking(i, tmp):
    global cnt
    # 정류장 위치를 벗어난다면 그만 (최소값과 비교)
    # 이 문제에서는 i가 n-1을 넘어갈 수 있기 때문에 부등호로 설정
    if i >= n-1:
        cnt = min(tmp, cnt)
        return
    # 시간초과를 막기 위해 더 작은 값이 안나오면 중지
    if tmp >= cnt:
        return

    # 한 번 충전해서 갈 수 있는 정류장 다 둘러보는 반복문
    else:
        for j in range(m[i]):
            # 그 경우의 수에 해당하는 곳으로 다시 옮겨서 재귀
            # i의 인덱스는 0부터 시작하므로 +1
            backtracking(i+j+1, tmp+1)


T = int(input())
for tc in range(1, T+1):
    n, *m = list(map(int, input().split()))

    # 3<=n<=100 0<m<n 이므로 최소값 다음과 같이 설정
    cnt = 100 * n
    # 시작할 때 충전하고 시작하므로 tmp 의 값을 미리 -1 해두기
    backtracking(0, -1)

    print(f'#{tc} {cnt}')

