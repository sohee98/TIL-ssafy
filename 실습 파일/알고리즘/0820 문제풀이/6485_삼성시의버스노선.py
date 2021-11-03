import sys
sys.stdin = open(f'6485input.txt', "r")
T = int(input())
for t in range(1, T+1):
    N = int(input())
    bus_stop = [0]*5001
    for n in range(N):
        a, b = map(int, input().split())
        while a <= b:
            bus_stop[a] += 1
            a += 1
    P = int(input())
    print('#{}'.format(t), end=' ')
    for _ in range(P):
        p = int(input())
        print(bus_stop[p], end=' ')
    print()

