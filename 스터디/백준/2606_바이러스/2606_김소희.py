N = int(input())
M = int(input())
net = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

virus = [0]*(N+1)
Q = [1]
while Q:
    i = Q.pop(0)
    if virus[i]:
        continue
    virus[i] = 1
    for j in range(len(net[i])):
        Q.append(net[i][j])
print(sum(virus)-1)