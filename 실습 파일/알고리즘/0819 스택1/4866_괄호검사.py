import sys
sys.stdin = open(f'4866sample_input.txt', "r")

T = int(input())
for t in range(1, T+1):
    code = input()
    ST = []
    result = 1
    for i in range(len(code)):
        if code[i] == '{':
            ST.append('{')
        if code[i] == '(':
            ST.append('(')
        if code[i] == '}':
            if ST and ST[-1]=='{':
                ST.pop(-1)
            else:
                result = 0
                break
        if code[i] == ')':
            if ST and ST[-1]=='(':
                ST.pop(-1)
            else:
                result = 0
                break
    if ST:
        result = 0
    print('#{} {}'.format(t, result))

