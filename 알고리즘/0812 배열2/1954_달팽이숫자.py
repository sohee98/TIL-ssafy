import sys
sys.stdin = open(f'1954input.txt', "r")
T = int(input())
for t in range(1, T+1):
    N = int(input())

    #(i,j) 오른-아래-왼-위쪽 순서 (i:세로, j:가로)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 1
    i, j = 0, -1
    k = 0
    arr = [[0]*N for _ in range(N)]

    while cnt <= N*N:
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k+1)%4
    print('#{}' .format(t))
    for i in range(N):
        for j in range(N):
            print('{}'.format(arr[i][j]), end=' ')
        print()
