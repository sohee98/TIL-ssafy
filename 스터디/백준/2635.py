def num():
    new = lst[-2]-lst[-1]
    if new >= 0:
        lst.append(new)
        num()
    return lst

N = int(input())
maxL = 0
for n in range(N+1):
    lst = [N, n]
    l = num()
    if len(l) > maxL:
        maxL = len(l)
        result = list(l)
print(maxL)
print(*result)