import sys
sys.stdin = open(f'4837sample_input.txt', "r")
T = int(input())
A = list(range(1, 13))
n = 12

def mySum(a):
    sumV = 0
    for i in a:
        sumV += i
    return sumV

for t in range(1, T+1):
    N, K = map(int, input().split())

    part_list = []
    sum_dic = {}                   # {부분집합 합 : 갯수} 딕셔너리
    for i in range(1<<n):
        part = []
        for j in range(n+1):
            if i & (1<<j):
                part.append(A[j])
        if len(part) == N:
            if sum_dic.get(mySum(part)):
                sum_dic[mySum(part)] += 1
            else:
                sum_dic[mySum(part)] = 1
    if sum_dic.get(K):
        print('#{} {}' .format(t, sum_dic[K]))
    else:
        print('#{} 0' .format(t))



