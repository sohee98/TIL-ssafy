import sys
sys.stdin = open("4828sample_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    maxV = 0
    minV = ai[0]

    for i in range(N):
        if ai[i] > maxV:
            maxV = ai[i]
        if ai[i] < minV:
            minV = ai[i]
    result = maxV - minV
    print('#{} {}'.format(t, result))