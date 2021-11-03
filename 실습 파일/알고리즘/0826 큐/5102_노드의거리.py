import sys
sys.stdin = open(f'5102sample_input.txt', "r")
def bfs_G(s, g):
    q = []                  # 큐 생성
    visited = [0]*(V+1)     # visited 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 visited 표시
    while q:
        v = q.pop(0)
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1
    if visited[g]:
        return visited[g] - 1
    else:
        return 0


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    s, g = map(int, input().split())
    print('#{} {}'.format(t, bfs_G(s, g)))










