import sys
sys.stdin = open(f'1961input.txt', "r")

def rotate(lst):
    new = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new[i][j] = str(lst[N-j-1][i])
    return new

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    new = [[0]*N for _ in range(N)]
    result = [[0]*3 for _ in range(N)]
    for n in range(3):
        num_list = rotate(num_list)
        for i in range(N):
            result[i][n] = ''.join(num_list[i])

    print('#{}'.format(t))
    for end in range(N):
        print(*result[end])