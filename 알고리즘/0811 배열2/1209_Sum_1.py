import sys
sys.stdin = open("1209input.txt", "r")

def myMax(a, b, M):
    if a > M:
        M = a
    if b > M:
        M = b
    return M

T = 10
for t in range(T):
    tc = int(input())
    N = 100
    ARR = [list(map(int, input().split())) for _ in range(N)]
    sum_diag1 = sum_diag2 = 0
    resultMax = 0
    for i in range(N):
        sum_diag1 += ARR[i][i]
        sum_diag2 += ARR[i][N-i-1]
        sum_row = sum_col = 0
        for j in range(N):
            sum_row += ARR[i][j]
            sum_col += ARR[j][i]
        resultMax = myMax(sum_row, sum_col, resultMax)
    resultMax = myMax(sum_diag1, sum_diag2, resultMax)

    print('#{} {}'.format(tc, resultMax))

