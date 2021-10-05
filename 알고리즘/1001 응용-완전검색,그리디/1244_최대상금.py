import sys
sys.stdin = open(f'1244input.txt', "r")

# 32888 2

def change(lst, k):
    global maxV
    if k == 0:
        if int(''.join(lst)) > maxV:
            maxV = int(''.join(lst))
        return
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            lst[i], lst[j] = lst[j], lst[i]
            tmpN = int(''.join(lst))
            if num_dict.get((tmpN, k-1)):
                pass
            else:
                num_dict[(tmpN, k-1)] = 1
                change(lst, k-1)
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for tc in range(1, T+1):
    num, c = map(int, input().split())  # 숫자, 교환가능횟수
    numL = [n for n in str(num)]
    maxV = num
    num_dict = {}
    change(numL, c)
    print('#{} {}'.format(tc, maxV))







