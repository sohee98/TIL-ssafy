"""
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""

def prim():
    s = 0       # start
    D[s][0] = 0
    while len(U) <= N:
        # D의 key값이 최소이고 U에 포함되지 않은 정점을 구한다.
        minV = 1000000
        for i in range(N+1):
            if i in U: continue
            if D[i][0] < minV:
                minV = D[i][0]
                curV = i
        # U에 추가
        U.append(curV)

        # curV의 인접한 정점의 가중치를 사용하여 D를 업데이트
        for i in range(N+1):
            if i in U: continue
            if G[curV][i] > 0:
                if D[i][0] > G[curV][i]:
                    D[i][0] = G[curV][i]    # G[curV]에서 가장 작은값
                    D[i][1] = curV

N, E = map(int, input().split())
G = [[0]*(N+1) for _ in range(N+1)]
for i in range(E):
    s1, s2, w = map(int, input().split())
    G[s1][s2] = w
    G[s2][s1] = w

D = [[1000000, 0] for _ in range(N+1)]  # 0:key, 1:pi
U = []
prim()
print(G)
print(D)
print(U)
