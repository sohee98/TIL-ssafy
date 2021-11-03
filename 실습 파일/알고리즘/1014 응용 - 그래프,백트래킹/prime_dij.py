'''
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
'''

from queue import PriorityQueue

def prime(s):
    D[s][0] = 0
    D[s][1] = 0

    for k in range(N+1):
        minV = 1000000
        for i in range(N+1):
            if i in U: continue
            if D[i][0] < minV:
                curV = i
                minV = D[i][0]

        U.append(curV)

        for w, dis in adj[curV]:
            if w in U: continue
            if D[w][0] > dis:
                D[w][0] = dis
                D[w][1] = curV

        print(D)

def dijk(s):
    D[s][0] = 0
    D[s][1] = 0
    curV = s

    '''
    U = [s]
    for i in range(N):
        v, dis = adj[curV][i]
        D[w][0] = dis
    '''
    for k in range(N+1):
        minV = 1000000
        for i in range(N+1):
            if i in U: continue
            if D[i][0] < minV:
                curV = i
                minV = D[i][0]

        U.append(curV)

        for v, dis in adj[curV]:
            #if v in U: continue
            if D[v][0] > D[curV][0] + dis:
                D[v][0] = D[curV][0] + dis
                D[v][1] = curV

        print(D)

def dijP(s):
    D[s] = 0
    curV = s

    que = PriorityQueue()
    que.put((0,0))
    while not que.empty():
        k, curV = que.get()
        U.append(curV)
        for w, dis in adj[curV]:
            if w in U: continue
            if D[w] > D[curV] + dis:
                D[w] = D[curV] + dis
                que.put((D[w], w))
    print(D)

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for i in range(M):
    S, E, V = map(int, input().split())
    adj[S].append([E, V])
    adj[E].append([S, V])

D = [[1000000, -1] for _ in range(N+1)]
U = []
prime(0)

D = [[1000000, -1] for _ in range(N+1)]
U = []
dijk(0)

D = [1000000] * (N+1)
U = []
dijP(0)



