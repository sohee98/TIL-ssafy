import sys
for i in range(1, 6):
    sys.stdin = open(f'./섹션3_입출력/6. 격자판 최대합/in{i}.txt', "r")
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    def myMax(lst):
        maxV = 0
        for i in range(len(lst)):
            if lst[i] > maxV:
                maxV = lst[i]
        return maxV

    def maxSum(lst):
        n = len(lst)
        sum_list = []
        for i in range(n):
            sumV1 = sumV2 = 0
            for j in range(n):
                sumV1 += lst[i][j]
                sumV2 += lst[j][i]
            sum_list.append(sumV1)
            sum_list.append(sumV2)
        sumV3 = sumV4 = 0
        for i in range(n):
            sumV3 += lst[i][i]
            sumV4 += lst[i][n-i-1]
        sum_list.append(sumV3)
        sum_list.append(sumV4)
        return myMax(sum_list)

    print('#{} {}' .format(i, maxSum(num)))