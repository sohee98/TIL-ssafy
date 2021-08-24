# 연습문제1
S = '2+3*4/5'

def postfix(S):
    ST = []
    P = []
    for s in S:
        if s.isdigit():
           P.append(s)
        else:
           ST.append(s)
    while ST:
        P.append(ST.pop(-1))
    return ''.join(P)

print(postfix(S))


##
def step1(s):
    isp = {'*':2, '+':1}
    t = []
    ST = []
    for c in s:
        if c.isdecimal():
            t.append(c)
        else:
            if len(ST) == 0 or isp[ST[-1]] < isp[c]:    # '+'   c:'*'
                ST.append(c)
            else:
                while ST and isp[ST[-1]] >= isp[c]:     # '+''*'   c:'*'
                    t.append(ST.pop())
    while ST:
        t.append(ST.pop(-1))
    return t

def step2(t):
    ST = []
    for c in t:
        if c.isdecimal():
            ST.append(c)
        else:
            n1 = ST.pop()
            n2 = ST.pop()
            if c == '+':
                ST.append(n1+n2)
            if c == '*':
                ST.append(n1*n2)
    return ST.pop()

