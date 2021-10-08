import sys
sys.stdin = open(f'1486input.txt', "r")

def solve(k, sumV, rs):     # rs:남은 값들의 합
    global minV
    if sumV + rs < B or sumV >= minV:   # 가지치기
        return
    if B <= sumV < minV:
        minV = sumV
        return
    for i in range(N):
        if not v[i]:
            v[i] = 1
            solve(k+1, sumV+p[i], rs-p[i])
            v[i] = 0
        else:
            rs -= p[i]

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())        # N:점원수, B:선반높이
    p = list(map(int, input().split()))
    v = [0]*N
    minV = 2000000
    # print(p)
    solve(0, 0, sum(p))
    print('#{} {}'.format(tc,minV-B))