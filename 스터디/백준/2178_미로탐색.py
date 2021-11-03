N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(N):
    S = input()
    for s in S:
       arr[i].append(int(s))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
ST = [(0,0)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
cnt = 1
i = j = 0
minV = N*M
def maze(i, j, cnt):
    global minV

    if cnt+1 > minV:
        return

    if i == N-1 and j == M-1:
        if cnt+1 < minV:
            minV = cnt+1
        return
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] and not visited[ni][nj]:
            visited[ni][nj] = 1
            maze(ni, nj, cnt+1)
            visited[ni][nj] = 0
maze(0, 0, 0)
print(minV)


# BFS
# def bfs(s):
#     Q = []
#     Q.append(s)
#     visited[s] = True
#     while Q:
#         s = Q.pop(0)
#         print(s, end=' ')
#         for i in grp2[s]:
#             if not visited[i]:
#                 Q.append(i)
#                 visited[i] = True
#     return