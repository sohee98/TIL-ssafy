di = [-1, 1, 0, 0]
dj = [0, 0, -1 ,1]
def count(i, j):
    global cnt
    visited[i][j] = 1
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and not visited[ni][nj]:
            count(ni, nj)
            return
    else:
        cnt += 1
        return

T = int(input())
for tc in range(1, 1+T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]     # 배추밭 세로N * 가로M
    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                count(i, j)
    print(cnt)