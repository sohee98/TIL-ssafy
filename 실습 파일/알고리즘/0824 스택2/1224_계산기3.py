import sys
sys.stdin = open(f'1224input.txt', "r")
def step1(s):
    isp = {'*':2, '+':1, '(':0}
    icp = {'*':2, '+':1, '(':3}
    t = []
    ST = []
    for c in s:
        if c.isdecimal():
            t.append(c)
        elif c == ')':
            while len(ST)>=2:
                t.append(ST.pop())
                if ST[-1]=='(':
                    ST.pop()
                    break
        else:
            if len(ST) == 0 or isp[ST[-1]] < icp[c]:    # '+'/'('   c:'*'/'+'
                ST.append(c)
            else:
                while ST and isp[ST[-1]] >= icp[c]:     # '+''*'   c:'*'
                    t.append(ST.pop())
                ST.append(c)

    while ST:
        t.append(ST.pop(-1))
    return t

def step2(t):
    ST = []
    for c in t:
        if c.isdecimal():
            ST.append(c)
        else:
            if len(ST) >= 2:
                n1 = int(ST.pop())
                n2 = int(ST.pop())
                if c == '+':
                    ST.append(n1+n2)
                if c == '*':
                    ST.append(n1*n2)
    return ST.pop()

T = 10
for t in range(1, T+1):
    N = int(input())
    tc = input()
    s1 = step1(tc)
    s2 = step2(s1)
    print('#{} {}'.format(t, s2))


