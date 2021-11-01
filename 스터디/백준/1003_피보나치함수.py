def fibonacci(k, memo, count0, count1):
    if memo[k]:
        return memo[k], count0[k], count1[k]
    if k == 0:
        return 0, 1, 0
    elif k == 1:
        return 1, 0, 1
    else:
        m1, c01, c11 = fibonacci(k-1, memo, count0, count1)
        m2, c02, c12 = fibonacci(k-2, memo, count0, count1)
        memo[k], count0[k], count1[k] = m1+m2, c01+c02, c11+c12
        return memo[k], count0[k], count1[k]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    memo = [[] for _ in range(41)]
    count0 = [0]*41
    count1 = [0]*41
    n, c0, c1 = fibonacci(N, memo, count0, count1)
    print(c0, c1)
