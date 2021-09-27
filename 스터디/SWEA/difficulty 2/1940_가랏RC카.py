T = int(input())
for t in range(1, T+1):
    N = int(input())
    ms = 0      # 속도
    l = 0       # 거리
    for _ in range(N):
        com = list(map(int, input().split()))
        if com[0] == 1:     # 가속
            ms += com[1]
        if com[0] == 2:     # 감속
            ms -= com[1]
            if ms < 0:
                ms = 0
        l += ms
    print('#{} {}'.format(t, l))