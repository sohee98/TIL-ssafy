# https://itcrowd2016.tistory.com/81
import sys
for i in range(1, 6):
    sys.stdin=open(f'./섹션2_입출력/1. k번째 약수/in{i}.txt', "r")
    n, k=map(int, input().split())

    num = []
    for j in range(1, n+1):
        if n%j == 0:
            num.append(j)
    if len(num) >= k:
        print(num[k-1])
    else:
        print('-1')