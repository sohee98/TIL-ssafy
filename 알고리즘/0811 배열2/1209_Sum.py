import sys
sys.stdin = open("1209input.txt", "r")

def myMax(inp):
    maxV = 0
    for i in range(len(inp)):
        if inp[i] > maxV:
            maxV = inp[i]
    return maxV

T = 10
for t in range(T):
    tc = int(input())
    ARR = [list(map(int, input().split())) for _ in range(100)]
    N = len(ARR)
    sum_list = []
    sum_diag1 = sum_diag2 = 0
    for i in range(N):
        sum_diag1 += ARR[i][i]
        sum_diag2 += ARR[i][N-i-1]
        sum_row = sum_col = 0
        for j in range(N):
            sum_row += ARR[i][j]
            sum_col += ARR[j][i]
        sum_list.append(sum_row)
        sum_list.append(sum_col)
    sum_list.append(sum_diag1)
    sum_list.append(sum_diag2)
    result = myMax(sum_list)

    print('#{} {}'.format(tc, result))

