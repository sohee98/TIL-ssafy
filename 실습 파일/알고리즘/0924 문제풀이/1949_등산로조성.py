import sys
sys.stdin = open(f'1949sample_input.txt', "r")
T = int(input())

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1. 현재 위치를 들고 다니지 않을 때
# r, c 좌표, road:지금까지 조성된 등산로의 길이, skill 공사 유무
def work(r, c, road, skill):
    global cnt
    if road > cnt : cnt = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
            # 현위치보다 낮은 곳으로 이동할 때
            if NN[r][c] > NN[nr][nc]:
                work(nr, nc, road+1, skill)
            # 현위치보다 높거나 같은 곳으로 이동할 때
            elif skill and NN[r][c] > NN[nr][nc] - K:
                tmp = NN[nr][nc]            # 기록
                NN[nr][nc] = NN[r][c] - 1
                work(nr, nc, road+1, 0)     # 스킬 사용
                NN[nr][nc] = tmp            # 원상복구

    visited[r][c] = 0

# 2. 현재 위치를 들고 다닐 때
def work2(r, c, h, road, skill):
    global cnt
    if road > cnt: cnt = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr<0 or nr>=N or nc<0 or nc>=N or visited[nr][nc]:
            continue
        if h > NN[nr][nc]:
            work2(nr, nc, NN[nr][nc], road+1, skill)
        elif skill and h > NN[nr][nc] - K:
            work2(nr, nc, NN[r][c]-1, road+1, 0)

    visited[r][c] = 0


for t in range(1, T+1):
    N, K = map(int, input().split())
    NN = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    maxH = 0
    for i in range(N):
        for j in range(N):
            if NN[i][j] > maxH:
                maxH = NN[i][j]     # 최대값 찾기
    cnt = 0
    uK = False          # 공사 했는지 여부
    result = []
    for i in range(N):
        for j in range(N):
            if NN[i][j] == maxH:
                # work(i, j, 1, 1)    # 좌표, 길, 스킬
                work2(i, j, maxH, 1, 1)     # 좌표, 높이, 길, 스킬

    print('#{} {}'.format(t, cnt))














