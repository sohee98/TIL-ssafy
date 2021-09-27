N = int(input())
cnt = 0
result = False
minV = 2000
if N % 3 == 0:
    minV = N // 3
    result = True
while True:
    N -= 5
    cnt += 1
    if N < 0:
        break
    if N % 3 == 0:
        minV = N//3 + cnt
        result = True
    if N == 0:
        minV = cnt
        result = True
        break


if result:
    print(minV)
else:
    print(-1)