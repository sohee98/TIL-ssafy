# U R D L
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
direction = ['U', 'R', 'D', 'L']
S1 = [3, 2, 1, 0]
S2 = [1, 0, 3, 2]

def dfs(i, j, cnt, d):
    global result, isInfinite

    while True:
        if cnt > 0 and i == PR-1 and j == PC-1:
            isInfinite = True
            return

        if i < 0 or i >= N or j < 0 or j >= M or arr[i][j] == 'C':
            result = cnt
            return

        if arr[i][j] == '\\':     # 0-3, 1-2, 2-1, 3-0
            i += di[S1[d]]
            j += dj[S1[d]]
            cnt += 1
            d = S1[d]

        elif arr[i][j] == '/':     # 0-1, 1-0, 2-3, 3-2
            i += di[S2[d]]
            j += dj[S2[d]]
            cnt += 1
            d = S2[d]

        else:
            i += di[d]
            j += dj[d]
            cnt += 1

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input())
PR, PC = map(int, input().split())

maxV = 0
for i in range(4):
    isInfinite = False
    dfs(PR-1+di[i], PC-1+dj[i], 1, i)
    if isInfinite:
        maxD = i
        maxV = 'Voyager'
        break
    if result > maxV:
        maxD = i
        maxV = result
print(direction[maxD])
print(maxV)

