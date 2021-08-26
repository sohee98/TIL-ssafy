import sys
sys.stdin = open(f'5099sample_input.txt', "r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    pizza = [[] for _ in range(len(Ci))]
    for i in range(len(Ci)):
        pizza[i] = [Ci[i], i+1]
    now = []
    for i in range(N):
        now.append(pizza.pop(0))
    while True:
        ci = now.pop(0)
        c = ci[0]
        i = ci[1]
        if c//2 > 0:
            now.append([c//2, i])
        if c//2 == 0 and pizza:
            now.append(pizza.pop(0))
        if len(pizza)==0 and len(now)==1:
            print('#{} {}'.format(t, now[0][1]))
            break
