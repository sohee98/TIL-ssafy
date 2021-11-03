import sys
sys.stdin = open(f'5204sample_input.txt', "r")

def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) or r < len(right):
        if l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        elif l < len(left):
            result.extend(left[l:])
            return result
        elif r < len(right):
            result.extend(right[r:])
            return result

def merge_sort(lst):
    global cnt
    if len(lst) == 1:
        return lst
    m = len(lst)//2
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])
    if left[-1] > right[-1]:
        cnt += 1
    res = merge(left, right)
    return res


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    numS = merge_sort(num)
    print('#{} {} {}'.format(tc, numS[N//2], cnt))