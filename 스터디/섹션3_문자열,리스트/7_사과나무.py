import sys
for t in range(1, 6):
    sys.stdin = open(f'./섹션3_입출력/7. 사과나무/in{t}.txt', "r")
    N = int(input())
    farm = [list(map(int, input().split())) for _ in range(N)]
    apple = 0
    i = 0
    while i <= N//2:
        apple += farm[i][N//2]
        for a in range(1,i+1):
            apple += farm[i][N//2-a] + farm[i][N//2+a]
        i += 1
    i = N//2 + 1
    while N//2 < i < N:
        apple += farm[i][N//2]
        for a in range(1, N-i):
            apple += farm[i][N//2-a] + farm[i][N//2+a]
        i += 1
    print('#{} {}'.format(t, apple))
