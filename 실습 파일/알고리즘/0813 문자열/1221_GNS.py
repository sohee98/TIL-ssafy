import sys
sys.stdin = open(f'1221input.txt', "r")

def getIndex(a, lst):
    for i in range(len(lst)):
        if lst[i] == a:
            ID = i
    return ID

T = int(input())
for t in range(T):
    test_num, test_len = input().split()
    test_len = int(test_len)
    test = list(input().split())
    sort_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    new_dic = {}
    for s in test:
        ind = getIndex(s, sort_list)
        if new_dic.get(ind):
            new_dic[ind] += 1
        else:
            new_dic[ind] = 1

    result = []
    number = 0
    while number < 10:
        for num, cnt in new_dic.items():
            if num == number:
                result.append(f"{sort_list[num]} " * cnt)
                number += 1

    print('{}'.format(test_num), end=' ')
    for i in range(10):
        print('{}' .format(result[i]), end=' ')
    print()








