T = int(input())
def MaxMin(lst):
    maxV = 0
    minV = 10000
    for m in range(len(lst)):
        if maxV <= lst[m]:
            maxV = lst[m]
            maxI = m
        if minV >= lst[m]:
            minV = lst[m]
            minI = m
    return maxI, minI
def mySum(lst):
    sumV = 0
    for i in range(len(lst)):
        sumV += lst[i]
    return sumV

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    maxI, minI = MaxMin(numbers)
    numbers[maxI] = 0
    numbers[minI] = 0
    sumV = mySum(numbers)
    avgV = round(sumV / (len(numbers)-2))
    print('#{} {}'.format(tc, avgV))
