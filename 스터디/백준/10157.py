C, R = map(int, input().split())    # C가로, R세로
K = int(input())
N = [[0]*C for _ in range(R)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]  # 상 우 하 좌
n = 0
i = R   # 초기값
j = 0
if K <= C*R:
    while n <= K:
        for d in range(4):
            while 0<=i+dy[d]<R and 0<=j+dx[d]<C and N[i+dy[d]][j+dx[d]]==0:
                n += 1
                i += dy[d]
                j += dx[d]
                N[i][j] = n
                if n == K:
                    break
            if n == K:
                break
        if n==K:
            break
    print(j+1, R-i)
else:
    print(0)

