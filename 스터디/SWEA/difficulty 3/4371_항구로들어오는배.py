T = int(input())
for tc in range(1, T+1):
    N = int(input())
    day = [int(input()) for _ in range(N)]
    print(day)

    boat = [0]*N        # 배가 정해지면 1
    boat[0] = 1
    start = 0
    cnt = 0             # 배의 수
    while True:
        for i in range(1, N):
            if boat[i] == 0:    # 아직 배가 안정해졌으면
                d = day[i] - day[start]     # start 와의 차이 = 주기
                boat[i] = 1
                cnt += 1
                tmp = day[i]    # 주기에서 현재 마지막 배 == 주기계산 할때 빼야할 값
                for j in range(i+1,N):
                    if (day[j]-tmp) == d:
                        tmp = day[j]
                        boat[j] = 1
        start += 1
        if sum(boat)==N:
            break
    print('#{} {}'.format(tc,cnt))