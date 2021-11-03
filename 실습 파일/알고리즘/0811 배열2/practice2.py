import sys
sys.stdin = open("in2.txt", "r")

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    result = 0

    for i in range(1<<n):
        part = []
        for j in range(n+1):
            if i & (1<<j):
                part.append(arr[j])
        # print(part)                       # 부분집합 완성
        if part and sum(part) == 0:
            result = 1
    print('#{} {}' .format(t, result))
