def dfs(v):
    ST = []
    visited = [False] * 8
    ST.append(v)
    visited[v] = True
    while ST:
        v = ST.pop(-1)
        print(v)
        for w in G[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = True

def bfs_G(v):
    q = []                  # 큐 생성
    visited = [False]*8     # visited 생성
    q.append(v)             # 시작점 인큐
    visited[v] = 1          # 시작점 visited 표시
    while q:
        v = q.pop(0)
        print(v)
        for w in G[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = True

def bfs_G1(v):
    q = []                  # 큐 생성
    visited = [0]*8     # visited 생성
    q.append(v)             # 시작점 인큐
    visited[v] = 1          # 시작점 visited 표시
    while q:
        v = q.pop(0)
        print(v, visited[v])
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1

def bfs_adj(v):
    q = []                  # 큐 생성
    visited = [False]*8     # visited 생성
    q.append(v)             # 시작점 인큐
    visited[v] = 1          # 시작점 visited 표시
    while q:                    # 큐가 비어있지 않으면 (처리할 정점이 남아 있으면)
        v = q.pop(0)
        print(v)
        for w in range(len(adj[v])):         # t에 인접하고 미방문인 모든 i에 대해
            if adj[v][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] = True


lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = [[] for _ in range(8)]

adj = [[0]*8 for _ in range(8)]

for i in range(0, 16, 2):
    v1 = lst[i]
    v2 = lst[i+1]
    G[v1].append(v2)
    G[v2].append(v1)

    adj[v1][v2] = 1
    adj[v2][v1] = 1

# print(G)
# print(adj)

# bfs_G(1)
# bfs_adj(1)
dfs(1)
