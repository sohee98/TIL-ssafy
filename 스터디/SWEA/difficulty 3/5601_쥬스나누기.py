T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    print('#{}'.format(tc), end=' ')
    for _ in range(N):
        print('1/{}'.format(N), end=' ')
    print()
