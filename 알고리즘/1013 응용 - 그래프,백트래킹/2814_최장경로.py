import sys
sys.stdin = open(f'2814sample_input.txt', "r")

def dfs(s, k):          # s:정점, k:길이
    global maxV
    if k > maxV:
        maxV = k

    if not visited[s]:
        visited[s] = 1
        for i in D[s]:
            dfs(i, k+1)
        visited[s] = 0
    else:
        return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    D = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        D[x].append(y)
        D[y].append(x)
    maxV = 1
    for i in range(1, N+1):
        visited = [0] * (N + 1)
        dfs(i, 0)
    print('#{} {}'.format(tc, maxV))

