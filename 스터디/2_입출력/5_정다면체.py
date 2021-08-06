import sys
for i in range(1,6):
    sys.stdin=open(f'./섹션2_입출력/5. 정다면체/in{i}.txt', "r")
    N, M = map(int, input().split())
    list_sum = []
    for n in range(1, N+1):
        for m in range(1, M+1):
            list_sum.append(n + m)
    count = 0
    list_count = []
    for num in range(1, N+M+1):
        list_count.append(list_sum.count(num))
    result = []
    for i in range(len(list_count)):
        if list_count[i] == max(list_count):
            result.append(i+1)
    print(*result)
