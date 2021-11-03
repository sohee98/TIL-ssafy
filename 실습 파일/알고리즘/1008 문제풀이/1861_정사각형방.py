import sys
sys.stdin = open(f'1861input.txt', "r")

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def find(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if ARR[nr][nc] - ARR[r][c] == 1:
            return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    room = [0]*(N*N+1)        # index=방번호, 이동할 수 있는 방이 있으면 1
    for i in range(N):
        for j in range(N):
            if find(i, j):
                room[ARR[i][j]] = 1
    cnt = 1
    maxV = 0
    maxI = idx = 0
    # print(room)
    for r in range(1, N*N):
        if room[r]:
            if cnt == 1:    # 첫번째 방
                idx = r
            cnt += 1
            if r == N*N-1:
                if maxV < cnt:
                    maxV = cnt
                    maxI = idx
        else:
            if maxV < cnt:
                maxV = cnt
                maxI = idx
            cnt = 1
    print('#{} {} {}'.format(tc, maxI, maxV))
