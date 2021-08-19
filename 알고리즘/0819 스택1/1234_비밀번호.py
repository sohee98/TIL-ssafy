import sys
sys.stdin = open(f'1234input.txt', "r")

def remove(LS):
    for i in range(1, len(LS)):
        if LS[i-1] == LS[i]:
            LS.pop(i)
            LS.pop(i-1)
            break
    else:
        return 0, LS
    return LS

T = 10
for t in range(1, T+1):
    N, pw = input().split()
    N = int(N)
    PW = [str(p) for p in pw]
    while True:
        newPW = remove(PW)
        if newPW[0] == 0:
            result = newPW[1]
            break
    print('#{} {}'.format(t, ''.join(result)))