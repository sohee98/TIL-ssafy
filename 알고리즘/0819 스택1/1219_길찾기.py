import sys
sys.stdin = open(f'1219input.txt', "r")

def dfs():
    visited = [0] * 100
    st = 0
    s = [st]
    visited[st] = True
    while s:
        st = s.pop(-1)
        if P1[st] or P2[st]:
            if not visited[P1[st]]:
                s.append(P1[st])
                visited[P1[st]] = True
            if P2[st] and not visited[P2[st]]:
                s.append(P2[st])
                visited[P2[st]] = True
    if visited[99]:
        return 1
    else:
        return 0

T = 10
for t in range(1, T+1):
    tc, N = map(int, input().split())
    I = list(map(int, input().split()))
    P1 = [[] for _ in range(100)]
    P2 = [[] for _ in range(100)]
    for i in range(0, len(I), 2):
        if P1[I[i]]:
            P2[I[i]] = I[i+1]
        else:
            P1[I[i]] = I[i+1]
    result = dfs()
    print('#{} {}'.format(t, result))