import sys
sys.stdin = open(f'4873sample_input.txt', "r")

def remove(LS):
    for i in range(1, len(LS)):
        if LS[i-1] == LS[i]:
            LS.pop(i)
            LS.pop(i-1)
            break
    else:
        return 0, LS
    return LS

T = int(input())
for t in range(1, T+1):
    S = input()
    L = [str(s) for s in S]
    while True:
        newL = remove(L)
        if newL[0] == 0:
            result = newL[1]
            break
    print('#{} {}'.format(t, len(result)))