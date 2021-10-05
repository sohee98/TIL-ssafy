import sys
sys.stdin = open(f'5186sample_input.txt', "r")

T = int(input())
for tc in range(1, T+1):
    N= float(input())
    res = ''
    while N > 0:
        N *= 2
        if N >= 1:
            res += '1'
            N -= 1
        else:
            res += '0'
        if len(res) >= 13:
            res = 'overflow'
            break
    print("#{} {}".format(tc,res))