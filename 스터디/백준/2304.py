def myMax(lst):
    maxV = 0
    for m in range(len(lst)):
        if maxV < lst[m]:
            maxV = lst[m]
            maxI = m
    return maxV, maxI

N = int(input())
X = [0] * 1001
for n in range(N):
    a, b = map(int, input().split())
    X[a] = b
maxH, maxX = myMax(X)
area = 0
latest = 0
for i in range(maxX):
    if X[i] == [0] or X[i] < latest:
        area += latest
    if X[i] >= latest:
        latest = X[i]
        area += latest
area += maxH
latest = 0
for j in range(1000,maxX,-1):
    if X[j] == [0] or X[j] < latest:
        area += latest
    if X[j] >= latest:
        latest = X[j]
        area += latest
print(area)