
#(i,j) 오른-아래-왼-위쪽 순서 (i:세로, j:가로)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 5
cnt = 1
i, j = 0, -1
k = 0
arr = [[0]*5 for _ in range(N)]

while cnt <= N*N:
    ni, nj = i + di[k], j + dj[k]
    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
        arr[ni][nj] = cnt
        cnt += 1
        i, j = ni, nj
    else:
        k = (k+1)%4
print(arr)

