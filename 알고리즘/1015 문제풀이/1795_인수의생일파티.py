import sys
sys.stdin = open(f'1795input.txt', "r")

def dijkstra(adj):
    dist = [987654321] * (N + 1)
    visited = [False] * (N+1)     # 방문했는지
    s = X           # s : 시작점 = 파티장소
    dist[s] = 0
    visited[s] = True

    for i in range(N+1):
        if adj[s][i] > 0:
            dist[i] = adj[s][i]   # s->i 걸리는 시간 dist에 저장

    while sum(visited) < N:
        # dist의 값이 최소이고 방문하지 않은 정점을 구한다.
        minV = 1000000
        for i in range(N + 1):
            if visited[i]: continue
            if dist[i] < minV:
                minV = dist[i]
                curV = i

        visited[curV] = True        # 방문함

        # curV의 인접한 정점의 가중치를 사용하여 dist를 업데이트
        for i in range(N + 1):
            if visited[i]: continue
            if adj[curV][i] > 0:
                if dist[i] > dist[curV] + adj[curV][i]:  # 원래값 > 새로운 더한 값
                    dist[i] = dist[curV] + adj[curV][i]
    return dist



T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())     # N:사람수, M:간선수, X:생일파티집
    adj1 = [[0]*(N+1) for _ in range(N+1)]  # 원래입력(진출)
    adj2 = [[0]*(N+1) for _ in range(N+1)]  # 뒤집은입력(진입)

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c     # x -> y 가는데 걸리는 시간 = c
        adj2[y][x] = c

    # 다익스트라 호출
    dist1 = dijkstra(adj1)
    dist2 = dijkstra(adj2)

    maxV = 0
    for i in range(1, N+1):
        if dist1[i] + dist2[i] > maxV:
            maxV = dist1[i] + dist2[i]

    print('#{} {}'.format(tc, maxV))