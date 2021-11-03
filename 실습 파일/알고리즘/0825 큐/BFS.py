## BFS
"""
def BFS(G, v, n):           # 그래프 G, 탐색 시작점 v
    visited = [0]*(n+1)     # n:정점의 개수
    queue = []      # 큐 생성
    queue.append(v) # 시작점 v를 큐에 삽입
    visited[v] = 1
    while queue:            # 큐가 비어있지 않은 경우
        t = queue.pop(0)    # 큐의 첫번째 원소 반환
        visit(t)
        for i in G[t] :     # t와 연결된 모든 정점에 대해
            if not visited[i]:      # 방문되지 않은 곳이라면
                queue.append(i)     # 큐에 넣기
                visited[i] = visited[t] + 1     # n으로 부터 1만큼 이동
"""

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs1(s, V):
    q = []                  # 큐 생성
    visited = [0]*(V+1)     # visited 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 visited 표시
    while q:                    # 큐가 비어있지 않으면 (처리할 정점이 남아 있으면)
        t = q.pop(0)            # 디큐 (꺼내서)해서 t에 저장
        print(t)                # t에 대한 처리
        for i in range(1, V+1):         # t에 인접하고 미방문인 모든 i에 대해
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)             # enqueue(i)
                visited[i] = visited[t] + 1          # i visited 표시

def bfs2(s, V):
    q = []                  # 큐 생성
    visited = [0]*(V+1)     # visited 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 visited 표시
    while q:                    # 큐가 비어있지 않으면 (처리할 정점이 남아 있으면)
        t = q.pop(0)            # 디큐 (꺼내서)해서 t에 저장
        print(t)                # t에 대한 처리
        for i in adjList[t]:         # t에 인접하고 미방문인 모든 i에 대해
            if visited[i] == 0:
                q.append(i)             # enqueue(i)
                visited[i] = visited[t] + 1          # i visited 표시


V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]         # 인접행렬
adjList = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    # adj[n1][n2] = 1
    # adj[n2][n1] = 1

    adjList[n1].append(n2)
    adjList[n2].append(n1)

# bfs1(1, V)
bfs2(1, V)






