import sys
sys.stdin = open(f'4881sample_input.txt', "r")

def per(a, k, N, sumV):
    global minV
    if sumV > minV:
        return
    if k == N:
        if minV > sumV:
            minV = sumV
    else:
        for i in range(N):
            if not visited[i]:
                t[k] = i
                visited[i] = True
                per(a, k+1, N, sumV+a[k][i])
                visited[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    t = [-1] * N
    minV = 10*N
    per(ARR, 0, N, 0)
    print('#{} {}'.format(tc, minV))