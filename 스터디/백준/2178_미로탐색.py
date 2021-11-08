from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(N):
    S = input()
    for s in S:
       arr[i].append(int(s))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def bfs(i, j):
    Q = deque()
    Q.append((i, j))
    while Q:
        i, j = Q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[ni][nj]==0:
                continue
            if arr[ni][nj] == 1:
                arr[ni][nj] = arr[i][j] + 1
                Q.append((ni, nj))
    return arr[N-1][M-1]
print(bfs(0, 0))

