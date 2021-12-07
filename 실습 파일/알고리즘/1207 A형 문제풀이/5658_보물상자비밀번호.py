import sys
sys.stdin = open('5658sample_input.txt', 'r')

def calc(num):
    number = 0
    num = num[::-1]
    for i in range(len(num)):
        if num[i].isdigit():
            number += int(num[i])*(16**i)
        else:
            number += (ord(num[i])-55)*(16**i)
    return number

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    L = N//4    # 숫자의 길이, 한변의 길이
    h = input()
    h += h[:L]
    lst = []
    for s in range(L):  # L 회전까지
        for i in range(s, s+N-2, 3):
            lst.append(calc(h[i:i+L]))
        # tmp = h[-1]
        # h = tmp + h[:-1]

    # lst.sort(reverse=True)
    # same_num_cnt = 0
    # k = 1
    # while k < K:
    #     if lst[k] == lst[k-1]:
    #         same_num_cnt += 1
    #     k += 1
    # print(lst)
    # print(same_num_cnt)
    # print('#{} {}' .format(tc, lst[k-1+same_num_cnt]))

    result = list(set(lst))
    result.sort(reverse=True)
    # print(result)
    print('#{} {}' .format(tc, result[K-1]))

