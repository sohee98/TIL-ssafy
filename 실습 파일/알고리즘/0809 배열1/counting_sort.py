data = [0, 4, 1, 3, 1, 2, 4, 1]
M = 5
N = len(data)
counts = [0] * M
temp = [0] * N

for d in data:
    counts[d] = counts[d]+1

for i in range(1, M):
    counts[i] += counts[i-1]
    # [1, 4, 5, 6, 8]

for j in range(N-1, -1, -1):
    temp[counts[data[j]]-1] = data[j]
    counts[data[j]] -= 1

print(temp)

