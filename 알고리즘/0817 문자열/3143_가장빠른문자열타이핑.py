import sys
sys.stdin = open(f'3143sample_input.txt', "r")

T = int(input())
for t in range(1, T+1):
    A, B = input().split()
    a = len(A)
    b = len(B)
    cnt = 0
    i = 0
    while i <= a:
        if A[i:i+b] == B:
            cnt += 1
            i += b
        else:
            i += 1
    result = a-cnt*(b-1)
    print('#{} {}' .format(t, result))