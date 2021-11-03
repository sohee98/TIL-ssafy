import sys
sys.stdin = open(f'5202sample_input.txt', "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N-1,0,-1):       # 정렬
        for j in range(i):
            if time[j][0] > time[j+1][0]:
                time[j], time[j+1] = time[j+1], time[j]

    for i in range(N-1,0,-1):       # 시작시간이 같은 것들 정렬
        for j in range(i):
            if time[j][0] == time[j+1][0] and time[j][1] > time[j+1][1]:
                time[j], time[j+1] = time[j+1], time[j]


    curS = time[0][0]
    curE = time[0][1]
    cnt = 1
    for i in range(1, N):
        if time[i][0] >= curE:
            minE = 24
            for j in range(i, N):
                if time[j][1] < minE:
                    minE = time[j][1]
                    curS = time[j][0]
                    curE = time[j][1]
            cnt += 1

    print('#{} {}'.format(tc, cnt))

