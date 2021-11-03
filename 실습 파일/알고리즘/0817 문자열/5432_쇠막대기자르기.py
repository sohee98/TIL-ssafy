import sys
sys.stdin = open(f'5432sample_input.txt', "r")

T = int(input())
for t in range(1, T+1):
    test = input()
    start = end = 0
    result = 0
    for i in range(len(test)):
        if test[i] == '(':
            start += 1
        if test[i] == ')':
            end += 1
            if test[i-1] == '(':
                result += start-end
            else:
                result += 1
    print('#{} {}' .format(t, result))








