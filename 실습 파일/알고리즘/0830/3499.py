import sys
sys.stdin = open(f'3499sample_input.txt', "r")
T = int(input())
for t in range(1, T+1):
    N = int(input())
    card = list(input().split())
    c1 = card[:(N+1)//2]
    c2 = card[(N+1)//2:]
    result = []
    for i in range(N):
        if i%2==0:
            result.append(c1.pop(0))
        else:
            result.append(c2.pop(0))
    print('#{} {}'.format(t, ' '.join(result)))