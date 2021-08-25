import sys
sys.stdin = open(f'1225input.txt', "r")
T = 10
for tc in range(1, T+1):
    t = int(input())
    Q = list(map(int, input().split()))
    N = [1, 2, 3, 4, 5]
    i = 0
    while True:
        num = Q.pop(0)
        if num-N[i] > 0:
            Q.append(num-N[i])
        else:
            Q.append(0)
            break
        i = (i+1) % 5

    print('#{}' .format(t), end=' ')
    for n in Q:
        print('{}'.format(n), end=' ')
    print()





