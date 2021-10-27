N = int(input())
arr = [input() for _ in range(N)]
K = int(input())
if K == 1:
    res = arr
elif K == 2:
    res = []
    for i in range(N):
        res.append(arr[i][::-1])
else:
    res = []
    for i in range(N-1, -1, -1):
        res.append(arr[i])

for i in range(N):
    print(res[i])
