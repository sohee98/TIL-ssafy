import sys
sys.stdin = open(f'4875sample_input.txt', "r")
# 0상-1우-2하-3좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(curX, curY):
    ST = []
    ST.append((curX, curY))     # v : (curX, curY)
    A[curX][curY] = 1           # 방문 - 길을 벽(1)으로 바꿈
    while ST:
        (curX, curY) = ST.pop()
        for d in range(4):
            newX, newY = curX+dx[d], curY+dy[d]
            if 0<=newX<N and 0<=newY<N and A[newX][newY] == 0:
                ST.append((newX,newY))
                A[newX][newY] = 1
            elif 0<=newX<N and 0<=newY<N and A[newX][newY] == 3:
                return 1
    return 0
T = int(input())
for t in range(1, T+1):
    N = int(input())
    A = []
    for n in range(N):
        S = input()
        a = []
        for m in range(N):
            a.append(int(S[m]))
        A.append(a)

    for i in range(N):
        for j in range(N):
            if A[i][j] == 2:
                curX = i
                curY = j
            if A[i][j] == 3:
                endX = i
                endY = j

    print('#{} {}'.format(t,dfs(curX, curY)))





