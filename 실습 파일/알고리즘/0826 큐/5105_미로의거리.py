import sys
sys.stdin = open(f'5105sample_input.txt', "r")
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def bfs(x, y):
    q = []                  # 큐 생성
    visited = [[0]*N for _ in range(N)]     # visited 생성
    q.append((x, y))             # 시작점 인큐
    visited[x][y] = 1          # 시작점 visited 표시
    while q:
        (x, y) = q.pop(0)
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<=nx<N and 0<=ny<N and A[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
            elif 0<=nx<N and 0<=ny<N and A[nx][ny] == 3:
                return visited[x][y]-1
    return 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    A = []
    for n in range(N):
        S = input()
        a = []
        for m in range(N):
            a.append(int(S[m]))
        A.append(a)

    for i in range(N):
        for j in range(N):
            if A[i][j] == 2:
                curX = i
                curY = j
            if A[i][j] == 3:
                endX = i
                endY = j

    print('#{} {}'.format(t,bfs(curX, curY)))