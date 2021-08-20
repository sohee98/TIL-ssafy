import sys
sys.stdin = open(f'1979input.txt', "r")
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append([n for n in map(int, input().split())])
        P[i].append(0)
    P.append([0]*(N+1))
    ok = 0
    for i in range(N):
        cnt1 = 0
        cnt2 = 0
        for j in range(N):
            if P[i][j] == 1:            # 가로
                cnt1 += 1
                if P[i][j+1] == 0 and cnt1 == K:
                    ok += 1
                    cnt = 0
            else:
                cnt1 = 0
            if P[j][i] == 1:            # 세로
                cnt2 += 1
                if P[j+1][i] == 0 and cnt2 == K:
                    ok += 1
                    cnt2 = 0
            else:
                cnt2 = 0
    print('#{} {}'.format(t,ok))