import sys
sys.stdin = open(f'1244input.txt', "r")

def change(k):
    global maxV
    intV = int(''.join(lst))

    if k == c:
        if intV > maxV:
            maxV = intV
        return


    for i in range(720):
        if state[k][i] == 0:
            state[k][i] = intV
            break
        if state[k][i] == intV:
            return


    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            lst[i], lst[j] = lst[j], lst[i]
            change(k + 1)
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for tc in range(1, T+1):
    num, c = map(int, input().split())      # 숫자, 교환가능횟수
    lst = [n for n in str(num)]
    maxV = 0
    state = [[0]*720 for _ in range(c)]     #[k][720]
    change(0)
    print('#{} {}'.format(tc, maxV))







