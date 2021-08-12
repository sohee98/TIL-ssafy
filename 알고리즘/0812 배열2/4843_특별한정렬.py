import sys
sys.stdin = open(f'4843sample_input.txt', "r")
T = int(input())

def popMaxMin(lst):         # 최대/최소 반환, 원래 리스트에서 삭제
    MaxV = 0
    MinV = 100
    for i in range(len(lst)):
        if lst[i] > MaxV:
            MaxV = lst[i]
            MaxP = i
    lst.pop(MaxP)
    for i in range(len(lst)):
        if lst[i] < MinV:
                MinV = lst[i]
                MinP = i
    lst.pop(MinP)
    return MaxV, MinV

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    new = []
    for i in range(5):
        m, n = popMaxMin(arr)
        new.append(m)
        new.append(n)
    print('#{}'.format(t), end=' ')
    for p in range(len(new)):
        print('{}'.format(new[p]), end=' ')
    print()
