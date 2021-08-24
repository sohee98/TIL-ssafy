import sys
sys.stdin = open(f'1223input.txt', "r")
T = 10
for t in range(1, T+1):
    N = int(input())
    tc = input()

    def postfix(S):
        ST = []
        post = []
        for s in S:
            if s in ['+', '*']:
                if ST and s == '*' and ST[-1]=='+':
                    ST.append(s)
                else:
                    if ST:
                        post.append(ST.pop(-1))
                    ST.append(s)
            else:
                post.append(s)
        while ST:
            post.append(ST.pop(-1))
        return ''.join(post)

    def calculate(S):
        ST = []
        for s in S:
            if s.isdigit():
                ST.append(s)
            else:
                s2 = int(ST.pop(-1))
                s1 = int(ST.pop(-1))
                if s == '*':
                    ST.append(s1*s2)
                else:
                    ST.append(s1+s2)
        return ST.pop()

    tc_post = postfix(tc)
    print('#{} {}'.format(t, calculate(tc_post)))