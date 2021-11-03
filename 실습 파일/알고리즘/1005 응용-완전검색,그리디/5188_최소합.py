import sys
sys.stdin = open(f'5188sample_input.txt', "r")

def solve(i, j, sumV):
    global minV
    if i == N-1 and j == N-1:
        if sumV < minV:
            minV = sumV
        return
    if i + 1 < N:
        solve(i+1, j, sumV + ARR[i+1][j])
    if j + 1 < N:
        solve(i, j+1, sumV + ARR[i][j+1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    minV = 999
    solve(0, 0, ARR[0][0])
    print('#{} {}'.format(tc, minV))