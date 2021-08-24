import sys
for t in range(1, 6):
    sys.stdin = open(f"./섹션3_입출력/8. 곳감/in{t}.txt", "r")
    N = int(input())
    farm = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    move = [list(map(int, input().split())) for _ in range(M)]
    # 행번호, 방향(0-왼/1-우), 회전수
    for i in range(M):
        x = move[i][0] - 1
        y = move[i][2]
        before = farm.pop(x)
        after = []
        if move[i][1] == 1:
            y = N-y
        for _ in range(N):
            if y < N:
                after.append(before[y])
            else:
                y = N - y
                after.append(before[y])
            y += 1
        farm.insert(x, after)
    print(farm)
    cnt = 0
    i = 0
    while i <= N // 2:
        cnt += farm[i][N//2]
        for a in range(N//2, i, -1):
            cnt += farm[i][N // 2 - a] + farm[i][N // 2 + a]
        i += 1
    i = N // 2 + 1
    while N // 2 < i < N:
        cnt += farm[i][N//2]
        for a in range(1, i-N//2+1):
            cnt += farm[i][N // 2 - a] + farm[i][N // 2 + a]
        i += 1
    print(cnt)

