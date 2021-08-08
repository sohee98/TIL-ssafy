import sys
for i in range(1,6):
    sys.stdin=open(f'./섹션2_입출력/6. 자릿수의 합/in{i}.txt', "r")
    N = int(input())
    lst = input().split()
    sum_list = []
    for n in lst:
        sumV = 0
        for i in range(len(n)):
            sumV += int(n[i])
        sum_list.append(sumV)
    for n in range(N):
        if sum_list[n] == max(sum_list):
            print(lst[n])
            break
