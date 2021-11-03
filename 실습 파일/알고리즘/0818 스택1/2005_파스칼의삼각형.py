import sys
sys.stdin = open(f'2005input.txt', "r")

def pascal(p):
    new = []
    if p == 1:
        result_list = [[1]]
    else:
        result_list = pascal(p-1)
        new.append(1)
        for j in range(1, p-1):
            new.append(result_list[p-2][j-1] + result_list[p-2][j])
        new.append(1)
        result_list.append(new)
    return result_list

T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = pascal(N)
    print('#{}'.format(t))
    for n in range(N):
        print(*result[n])
