S = int(input())
N = 1
sumV = 0
while True:
    sumV += N
    if sumV >= S:
        break
    N += 1

if sumV == S:
    print(N)
else:
    print(N-1)

