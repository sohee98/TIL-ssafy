import sys
sys.stdin = open(f'1859input.txt', "r")

def myMax(lst):
    maxV = 0
    for i in range(len(lst)):
        if lst[i] >= maxV:
            maxV = lst[i]
            maxI = i
    return maxV, maxI

def maxBenefit(lst):
    benefit = 0
    maxPrice, maxI = myMax(lst)
    for i in range(maxI):
        benefit += maxPrice - price[i]
    if maxI != N-1:
        lst = lst[maxI+1:]
    else:
        lst = []
    return benefit, lst

T = int(input())
for t in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    result = 0
    while len(price) > 0:
        result += maxBenefit(price)[0]
        price = maxBenefit(price)[1]
    print('#{} {}' .format(t, result))
