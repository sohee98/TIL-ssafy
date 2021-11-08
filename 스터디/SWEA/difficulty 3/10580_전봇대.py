T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))

    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):   # 중복되지 않게 뒤의 전선들과 비교
            a, b = arr[i]           # a=시작점, b=끝점
            if a < arr[j][0] and b > arr[j][1]:     # 시작점보다 크고 끝점보다 작을 때
                cnt += 1
            elif a > arr[j][0] and b < arr[j][1]:   # 시작점보다 작고 끝점보다 클 때
                cnt += 1

    print('#{} {}'.format(tc, cnt))