N, A, B = map(int, input().split())
lst = range(1, N+1)
k = 1
while N:
    if A % 2 == 1 and B == A+1:
        result = k
        break
    A = (A+1)//2
    B = (B+1)//2
    k += 1
    N //= 2

# if not N:
#     result = -1

print(result)
