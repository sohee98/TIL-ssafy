import sys
sys.stdin = open(f'4869sample_input.txt', "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())

    ### 점화식 이용
    ## 1 - 재귀
    # def f(n):
    #     if n == 0 or n == 10:               # f(0) = 1, f(10) = 1
    #         return 1
    #     if n >= 20:                         # f(n) = f(n-10) + 2*f(n-20)
    #         return f(n-10) + 2*f(n-20)
    # print('#{} {}'.format(t, f(N)))

    ## 2 - DP
    n = N//10
    cnt = 0
    lst = [1, 1]
    for i in range(2, 31):
        cnt = lst[i-1] + 2*lst[i-2]
        lst.append(cnt)
    print('#{} {}'.format(t, lst[n]))


