T = int(input())

for i in range(1, T + 1):
    num = list(map(int, input().split()))
    avg = sum(num)/len(num)

    if avg - avg//1 < 0.5:
        avg = avg//1
    else:
        avg = avg//1 + 1
    print(f'#{i} {int(avg)}')
