import sys
sys.stdin = open(f'5248sample_input.txt', "r")

## 1. dfs
def dfs(i):
    visited[i] = True
    if G[i]:
        for j in G[i]:
            if not visited[j]:
                dfs(j)
    return

## 2. union
def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    ## 1. dfs
    G = [[] for _ in range(N+1)]
    for i in range(0, len(lst), 2):
        G[lst[i]].append(lst[i+1])
        G[lst[i+1]].append(lst[i])
    # print(G)
    visited = [False]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    # print('#{} {}'.format(tc, cnt))

    ## 2. union
    p = [i for i in range(N + 1)]       # [0, 1, 2, 3, 4]
    for i in range(M):
        s1 = lst[i * 2]
        s2 = lst[i * 2 + 1]
        union(s1, s2)
    # print(p)            # index 마다 각 조별 대표가 나타남
    cnt = [0] * (N+1)
    for i in range(1, N+1):
        cnt[find_set(i)] = 1    # 대표자에 1로 표시
    print('#{} {}'.format(tc, sum(cnt)))




