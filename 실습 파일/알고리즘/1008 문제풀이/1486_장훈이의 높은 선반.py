import sys
sys.stdin = open(f'1486input.txt', "r")

# 시간초과 뜸
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

def solve2(N):
    global minV
    for x in range(2**N):       # 부분집합구하기
        out = ''
        for i in range(N-1, -1, -1):
            if x & (1 << i):
                out += '1'
            else:
                out += '0'
    sumV = 0
    for b in range(N):
        if out[b] == '1':
            sumV += p[b]
            if sumV >= B:
                if sumV <= minV:
                    minV = sumV
                else:
                    break

def solve3(k, sumV):
    global minV
    if sumV >= minV:
        return
    if k >= N:
        if sumV >= B:
            minV = sumV
        return
    else:
        solve3(k+1, sumV+p[k])
        solve3(k+1, sumV)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())        # N:점원수, B:선반높이
    p = list(map(int, input().split()))
    v = [0]*N
    minV = 2000000
    # solve(0, 0, sum(p))
    # solve2(N)
    solve3(0, 0)
    print('#{} {}'.format(tc,minV-B))