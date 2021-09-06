import sys
for t in range(1, 6):
    sys.stdin = open(f"./섹션3_입출력/9. 봉우리/in{t}.txt", "r")
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        m[i].append(0)
        m[i].insert(0,0)
    m.insert(0, [0]*(N+2))
    m.append([0] * (N+2))
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if m[i][j] > m[i-1][j] and m[i][j] > m[i+1][j] and m[i][j] > m[i][j-1] and m[i][j] > m[i][j+1]:
                cnt += 1
    print('#{} {}' .format(t, cnt))