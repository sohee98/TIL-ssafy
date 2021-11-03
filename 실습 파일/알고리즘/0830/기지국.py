# 싸피 1기 im 테스트 문제
# 기지국 문제 답안 코드

import sys
sys.stdin = open('기지국input.txt')

def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스체크, H일때 X로 바꾸기
        for j in range(ord(arr[x][y])-ord('A') + 1):
            if 0 <= nx < N and 0 <= ny < N :
                if arr[nx][ny] == 'H':
                    arr[nx][ny] = 'X'
                nx = nx + dx[i]
                ny = ny + dy[i]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 기지국 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
                check(i, j)
    # 4방향 돌려서 커버되는 H -> X
    # H 세기
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                ans += 1

    print("#{} {}".format(tc, ans))
    for i in arr:
        print(*i)