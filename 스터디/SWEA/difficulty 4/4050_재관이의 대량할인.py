T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    sumV = sum(lst)
    for i in range(2, N, 3):
        sumV -= lst[i]
    print('#{} {}'.format(tc, sumV))