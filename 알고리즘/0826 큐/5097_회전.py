import sys
sys.stdin = open(f'5097sample_input.txt', "r")
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    move = M % N
    for m in range(move):
        p = Q.pop(0)
        Q.append(p)
    print('#{} {}' .format(t, Q[0]))