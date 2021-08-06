T = int(input())

for i in range(1, T + 1):
    num = list(map(int, input().split()))
    for n in num:
        if n == max(num):
            print(f'#{i} {n}')
