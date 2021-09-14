T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [[] for _ in range(N)]
    for n in range(N):
        tmp = input()
        for t in tmp:
            farm[n].append(int(t))

    h = N//2
    S = 0
    i = 0
    while i <= h:
        S += sum(farm[i][h-i:h+i+1])
        i += 1
    while i < N:
        j = N-1-i
        S += sum(farm[i][h-j:h+j+1])
        i += 1
    print('#{} {}'.format(tc, S))
