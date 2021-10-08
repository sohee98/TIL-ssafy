import sys
sys.stdin = open(f'4366sample_input.txt', "r")

def toint(num, a):  # a진수(뒤집은거) 10진수로 바꾸기
    res = 0
    for i in range(len(num)):
        res += num[i] * a**i
    return res


T = int(input())
for tc in range(1, T+1):
    bin = input()   # 2진수
    ter = input()   # 3진수
    binR = list(map(int, bin))[::-1]    # 순서 뒤집은 리스트
    terR = list(map(int, ter))[::-1]
    b = toint(binR, 2)       # 10진수
    t = toint(terR, 3)
    bin_list = []
    ter_list = []
    for i in range(len(bin)):
        if binR[i] == 0:
            bin_list.append(b + 2**i)
        if binR[i] == 1:
            bin_list.append(b - 2**i)
    for i in range(len(ter)):
        if terR[i] == 0:
            ter_list.append(t + 3**i)       # 1일때
            ter_list.append(t + 2*(3**i))   # 2일때
        if terR[i] == 1:
            ter_list.append(t - 3**i)       # 0일때
            ter_list.append(t + 3**i)       # 2일때
        if terR[i] == 2:
            ter_list.append(t - 2*(3**i))   # 0일때
            ter_list.append(t - 3**i)       # 1일때

    for n in bin_list:
        if n in ter_list:
            answer = n
    print('#{} {}'.format(tc, answer))



