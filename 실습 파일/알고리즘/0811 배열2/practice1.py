import sys
sys.stdin = open("in1.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    result = 0
    for y in range(N):
        for x in range(N):
            num = []
            for mode in range(4):
                newx = x + dx[mode]
                newy = y + dy[mode]
                if 0 <= newx < N and 0 <= newy < N:
                    num.append(ARR[newy][newx])
                sumV = 0
                for n in range(len(num)):
                    sumV += abs(ARR[y][x]-num[n])
            result += sumV
    print('#{} {}' .format(t, result))