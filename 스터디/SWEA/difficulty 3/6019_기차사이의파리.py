T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    t = D / (A+B)   # 갈 수 있는 시간
    dis = F * t     # 거리 = 시간 * 속력
    print('#{} {}'.format(tc, dis))