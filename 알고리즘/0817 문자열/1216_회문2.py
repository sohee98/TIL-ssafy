import sys
sys.stdin = open(f'1216input.txt', "r")

def ispalindrome():
    for i in range(N):
        for j in range(N-M+1):
            test1 = str_list[i][j:j+M]
            if test1 == test1[::-1]:
                return M
            test2 = []
            for k in range(M):
                test2.append(str_list[j+k][i])
            test2 = ''.join(test2)
            if test2 == test2[::-1]:
                return M
    return 0

T = 10
for t in range(T):
    tc = int(input())
    N = 100
    str_list = [input() for _ in range(N)]
    result = 0
    for M in range(1, 101):
        if ispalindrome() > result:
            result = ispalindrome()
    print('#{} {}' .format(tc, result))

