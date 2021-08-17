import sys
sys.stdin = open(f'4864sample_input.txt', "r")

def findstr(str1, str2):
    N = len(str1)
    M = len(str2)

    for idx2 in range(M - N + 1):
        idx1 = 0
        while idx1 < N and str1[idx1] == str2[idx1 + idx2]:
            idx1 += 1
        if idx1 == N:  # 찾음
            return 1
        else:  # 못찾음
            idx2 += 1
    return 0

T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    print('#{} {}' .format(t, findstr(str1, str2)))

