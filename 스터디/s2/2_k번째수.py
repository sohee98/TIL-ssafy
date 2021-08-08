# https://itcrowd2016.tistory.com/81
import sys
for i in range(1, 6):
    sys.stdin=open(f'./섹션2_입출력/2. k번째 수/in{i}.txt', "r")
    T = int(input())
    for t in range(1, T+1):
        N, s, e, k = map(int, input().split())
        lst = list(map(int, input().split()))
        new_lst = lst[s-1:e]
        new_lst.sort()
        print(f'#{t} {new_lst[k-1]}')

    
