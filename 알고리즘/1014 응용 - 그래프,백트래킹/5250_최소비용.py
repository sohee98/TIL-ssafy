import sys
sys.stdin = open(f'5250sample_input.txt', "r")

from collections import deque

# dfs - 시간이 너무 오래걸림
# def dfs(i, j, cnt):
#     global maxV
#     if cnt > maxV:
#         return
#     if i == N-1 and j == N-1:
#         maxV = max(maxV, cnt)
#     ...

# Dijkstra 알고리즘
def solve():
    Q = deque()
    Q.append((0, 0))
    D[0][0] = 0
    while Q:
        curX, curY = Q.popleft()
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:   # 상하우좌
            newX = curX + dx
            newY = curY + dy
            if 0<=newX<N and 0<=newY<N:
                # cur지점과 new지점 사이의 연료량
                # if arr[newY][newX] > arr[curY][curX]:
                #     fuel = arr[newY][newX] - arr[curY][curX] + 1
                # else:
                #     fuel = 1
                fuel = max(arr[newY][newX]-arr[curY][curX], 0) + 1
                # D[newY][newX] = min(D[curY][curX]+fuel,  D[newY][newX])
                if D[newY][newX] > D[curY][curX]+fuel:
                    D[newY][newX] = D[curY][curX] + fuel
                    Q.append((newX, newY))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[N*N*1000] * N for _ in range(N)]
    solve()
    print('#{} {}'.format(tc, D[N-1][N-1]))