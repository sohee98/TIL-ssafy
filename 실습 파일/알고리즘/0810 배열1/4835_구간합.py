import sys
sys.stdin = open("4835sample_input.txt", "r")

def mySum(lst):
    sumV = 0
    for i in lst:
        sumV += i
    return sumV

def myMaxMin(lst):
    maxV = 0
    minV = lst[0]
    for m in range(len(lst)):
        if lst[m] > maxV:
            maxV = lst[m]
        if lst[m] < minV:
            minV = lst[m]
    return maxV, minV

T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    ai = list(map(int, input().split()))

    sum_list = []                       # 0~M개 숫자 순서대로 더하기
    for a in range(N-M+1):
        tmp_list = ai[a:a+M]
        sum_list.append(mySum(tmp_list))

    maxV, minV = myMaxMin(sum_list)
    answer = maxV - minV

    print('#{} {}'.format(t, answer))