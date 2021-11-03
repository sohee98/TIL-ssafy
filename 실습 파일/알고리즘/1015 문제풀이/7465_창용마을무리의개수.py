import sys
sys.stdin = open(f'7465s_input.txt', "r")

def dfs(i):
    visited[i] = True
    if G[i]:
        for j in range(len(G[i])):
            k = G[i][j]
            if not visited[k]:
                dfs(k)
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    # print(G)
    visited = [False]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print('#{} {}'.format(tc, cnt))



