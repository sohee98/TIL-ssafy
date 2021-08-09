import sys
sys.stdin = open("input1206.txt", "r")

T = 10
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    result = 0

    # for i in range(2, N-1):
    #     if lst[i-2] < lst[i] and lst[i-1] < lst[i] and lst[i] > lst[i+1] and lst[i] > lst[i+2]:
    #         diff = lst[i]
    #         for j in [-2, -1, 1, 2]:
    #             if lst[i] - lst[i+j] <= diff:
    #                 diff = lst[i] - lst[i+j]
    #         result += diff

    for i in range(2, N-2):
        maxD = 0
        for j in [-2, -1, 1, 2]:
            if lst[i+j] > maxD:
                maxD = lst[i+j]

        if lst[i] > maxD:
            result += lst[i] - maxD

    print(f'#{t} {result}')
