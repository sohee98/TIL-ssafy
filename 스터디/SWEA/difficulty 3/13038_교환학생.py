T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    start = []
    for j in range(7):
        if A[j]:
            start.append(j)

    minD = 100000*7
    for s in range(len(start)):
        i = start[s]
        day = 0
        n = N
        while n > 0:
            if A[i]:
                n -= 1
            day += 1
            i = (i+1) % 7    # 끝까지 확인하면 다시 처음으로
        if day < minD:
            minD = day
    print('#{} {}'.format(tc,minD))