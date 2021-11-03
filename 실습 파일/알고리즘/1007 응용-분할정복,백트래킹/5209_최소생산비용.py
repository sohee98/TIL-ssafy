import sys
sys.stdin = open(f'5209sample_input.txt', "r")

def solve(k=0, sumV=0):
    global minV
    if sumV >= minV:
        return

    if k == N:
        if sumV < minV:
            minV = sumV
        return
    for i in range(N):
        if not v[i]:
            v[i] = 1
            solve(k + 1, sumV+lst[k][i])
            v[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    minV = 1500
    solve()
    print('#{} {}'.format(tc, minV))
