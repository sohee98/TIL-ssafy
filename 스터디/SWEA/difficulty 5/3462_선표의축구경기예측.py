def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    # 90분 경기를 3분간격으로 나눔 -> 최대 30골
    # 1 - 모든팀 득점이 소수가 아닌 확률
    # = 1 - A팀 소수X * B팀 소수X
    # = 1 - (1-A팀 소수) * (1-B팀 소수)
    num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]    # 30까지의 소수
    A, B = A/100, B/100
    sumA, sumB = 0, 0
    for i in range(len(num)):
        a, b = 1, 1
        # 확률공식
        a *= fact(30)/(fact(30-num[i])*fact(num[i])) * A**num[i] * ((1-A)**(30-num[i]))
        b *= fact(30)/(fact(30-num[i])*fact(num[i])) * B**num[i] * ((1-B)**(30-num[i]))
        sumA += a
        sumB += b

    ans = round(1-(1-sumA)*(1-sumB), 5)
    print(f"#{tc} {ans:.5f}")