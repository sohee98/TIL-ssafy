import sys
sys.stdin = open(f'1210input.txt', "r")

def getIndex(a, lst):
    for i in range(len(lst)):
        if lst[i] == a:
            ID = i
    return ID

T = 10
for t in range(1, T+1):
    tc = int(input())
    ladder = []
    for l in range(100):
        ladder.append(list(map(int, input().split())))
    x_list = []
    for i in range(100):
        if ladder[0][i] == 1:
            x_list.append(i)
    for start in x_list:
        x = start
        y = 1
        while y < 99:
            if 0 <= x + 1 < 100 and ladder[y][x+1] == 1:
                x = x_list[getIndex(x, x_list)+1]
                y += 1
                continue
            if 0 <= x - 1 < 100 and ladder[y][x-1] == 1:
                x = x_list[getIndex(x, x_list)-1]
                y += 1
                continue
            else:
                y += 1

        if ladder[y][x] == 2:
            print('#{} {}'.format(t, start))