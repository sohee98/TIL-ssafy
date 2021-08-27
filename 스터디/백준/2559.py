N, K = map(int, input().split())
temp = list(map(int, input().split()))
t = 0
for d in range(K):
    t += temp[d]
maxS = t
for i in range(N-K):
    t += temp[i+K] - temp[i]
    if t > maxS:
        maxS = t
print(maxS)
