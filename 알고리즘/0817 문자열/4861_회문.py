import sys
sys.stdin = open(f'4861sample_input.txt', "r")

def isCheck(str1):
    if str1 == str1[::-1]:
        return True

def ispalindrome():
    for i in range(N):
        for j in range(N-M+1):
            test1 = str_list[i][j:j+M]      # 가로
            test2 = []                      # 세로
            for k in range(M):
                test2.append(str_list[j+k][i])
            test2 = ''.join(test2)
            if isCheck(test1):
                return test1
            if isCheck(test2):
                return test2

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    str_list = [input() for _ in range(N)]
    result = ispalindrome()

    print('#{} {}' .format(t, result))