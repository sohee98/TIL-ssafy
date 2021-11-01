T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    sumList = []
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                sumList.append(numbers[i]+numbers[j]+numbers[k])
    result = list(set(sumList))
    result.sort()
    print('#{} {}'.format(tc, result[-5]))