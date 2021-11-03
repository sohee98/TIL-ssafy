import sys
sys.stdin = open(f'4408sample_input.txt', "r")

def mymax(lst):
    maxV = 0
    for n in range(len(lst)):
        if maxV < lst[n]:
            maxV = lst[n]
    return maxV

def div(num):
    return (int(num)+1)//2

T = int(input())
for t in range(1, T+1):
    N = int(input())

    # students = [list(map(div, input().split())) for _ in range(N)]
    # road = [0] * 201
    # for i in range(N):
    #     if students[i][0] > students[i][1]:
    #         students[i][0], students[i][1] = students[i][1], students[i][0]
    #     for j in range(students[i][0], students[i][1]+1):
    #         road[j] += 1

    road = [0] * 201
    for i in range(N):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        r1 = (start + 1)//2
        r2 = (end + 1) // 2
        for j in range(r1, r2+1):
            road[j] += 1

    print('#{} {}'.format(t, mymax(road)))