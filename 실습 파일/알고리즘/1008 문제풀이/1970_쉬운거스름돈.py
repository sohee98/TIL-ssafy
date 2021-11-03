import sys
sys.stdin = open(f'1970input.txt', "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    coin = [0]*8
    for i in range(8):
        if N >= money[i]:
            coin[i] = N // money[i]
            N %= money[i]
    print('#{}'.format(tc))
    print(*coin)
