import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 최초의 무한대값 설정
    INF = 10000
    adjM = [[INF] * (N+1) for _ in range(N+1)]
    
    # 처음 비용은 0으로 설정
    adjM[0][0] = 0


    queue = deque()
    queue.append((0,0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 인접 지역으로 이동시 기본적으로 1만큼의 연료
                tmp = 1
                # 더 높은곳으로 이동하는 경우 높이 차이만큼 추가 연료 소비
                if arr[nx][ny] > arr[x][y]:
                    tmp += arr[nx][ny] - arr[x][y]
                
                # 연료 소비량 갱신하고 queue에 저장
                if adjM[nx][ny] > tmp + adjM[x][y]:
                    adjM[nx][ny] = tmp + adjM[x][y]
                    queue.append((nx,ny))

    print(f'#{tc} {adjM[N-1][N-1]}')

                    



    

