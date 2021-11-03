import sys
sys.stdin = open(f'4874sample_input.txt', "r")

def Forth(S):
    ST = []
    for s in S:
        if s == '.':
            if len(ST)>=2:
                return 'error'
            else:
                return ST.pop()
        if s.isdecimal():
            ST.append(s)
        else:
            if len(ST) >= 2:
                s2 = int(ST.pop())
                s1 = int(ST.pop())
                if s == '*':
                    ST.append(s1 * s2)
                elif s == '/':
                    ST.append(s1 // s2)
                elif s == '+':
                    ST.append(s1 + s2)
                else:
                    ST.append(s1 - s2)
            else:
                return 'error'

T = int(input())
for t in range(1, T+1):
    tc = input().split()
    print('#{} {}'.format(t, Forth(tc)))