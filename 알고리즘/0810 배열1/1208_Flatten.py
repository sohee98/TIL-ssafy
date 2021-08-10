import sys
sys.stdin = open("1208input.txt", "r")

def myMaxMin(lst):
    maxV = 0
    minV = 100
    for m in range(len(lst)):
        if lst[m] >= maxV:
            maxV = lst[m]
            max_index = m
        if lst[m] <= minV:
            minV = lst[m]
            min_index = m
    return maxV, max_index, minV, min_index

def dump(lst):
    max_box, maxI, min_box, minI = myMaxMin(lst)
    if max_box - min_box > 1:
        lst[maxI] -= 1
        lst[minI] += 1
    return max_box - min_box

T = 10
for t in range(1, T+1):
    D = int(input())
    boxes = list(map(int, input().split()))

    while D >= 0:
        answer = dump(boxes)
        D -= 1
    print('#{} {}'.format(t, answer))

