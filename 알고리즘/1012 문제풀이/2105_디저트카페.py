import sys
sys.stdin = open(f'2105sample_input.txt', "r")
def solve():
    for i in range(N-1):
        for j in range(N-1):
            for a in range(N-1):
                for b in range(N-1):    # a,b 길이
                    # 좌중에서 중상으로
                    for i in range(a):
                        nX = j+1
                        nY = i-1
                    # 중상에서 우중으로
                    # 우중에서 하중으로
                    # 하중에서 좌중으로
                    # 길이 확인

# 오른쪽아래, 위, 왼쪽위, 아래
di = [1, -1, -1, 1, 0]
dj = [1, 1, -1, -1, 0]

def solve2(d, i, j, k):
    global maxV, startI, startJ
    if i == startI and j == startJ and d == 3:
        maxV = max(maxV, k)
        return
    if d >= 4:
        return
    if 0<=i<N and 0<=j<N and not visited[D[i][j]]:
        visited[D[i][j]] = 1
        solve2(d, i+di[d], j+dj[d], k+1)            # 방향유지
        solve2(d+1, i+di[d+1], j+dj[d+1], k+1)      # 방향변경
        visited[D[i][j]] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*101   # 디저트 수 - 방문여부
    maxV = -1
    for i in range(1, N-1):
        for j in range(N-1):
            startI = i
            startJ = j
            solve2(0, i, j, 0)
    print('#{} {}'.format(tc, maxV))



