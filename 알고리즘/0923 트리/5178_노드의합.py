import sys
sys.stdin = open(f'5178sample_input.txt', "r")

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        i, n = map(int, input().split())
        tree[i] = n
    if N % 2:
        for i in range(N, 1, -2):
            tree[i//2] = tree[i]+tree[i-1]
    else:
        tree[N//2] = tree[N]
        for i in range(N-1, 1, -2):
            tree[i//2] = tree[i]+tree[i-1]

    print('#{} {}'.format(t, tree[L]))