import sys
sys.stdin = open(f'4871sample_input.txt', "r")

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    node = []
    ND = [[] for _ in range(V + 1)]
    for i in range(E):
        node += [list(map(int, input().split()))]
        ND[node[i][0]].append(node[i][1])
    S, G = map(int, input().split())

    visited = [0] * (V+1)
    def dfs(st, end):
        s = []
        s.append(st)
        visited[st] = True
        result = []
        while s:
            st = s.pop(-1)
            result.append(st)
            for w in ND[st]:
                if not visited[w]:
                    s.append(w)
                    visited[w] = True
        if end in result:
            return 1
        else:
            return 0
    result = dfs(S, G)
    print('#{} {}'.format(t, result))