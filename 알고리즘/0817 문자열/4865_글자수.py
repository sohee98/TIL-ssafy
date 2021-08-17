import sys
sys.stdin = open(f'4865sample_input.txt', "r")

T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    str2_dic = {}
    for i in str2:
        if str2_dic.get(i):
            str2_dic[i] += 1
        else:
            str2_dic[i] = 1
    result = 0
    for j in str1:
        if str2_dic.get(j) and str2_dic[j] > result:
            result = str2_dic[j]

    print('#{} {}' .format(t, result))