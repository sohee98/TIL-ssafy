A, B = map(int, input().split())
lst = []
i = 1
while True:
    for j in range(i):
        lst.append(i)
    i += 1
    if len(lst) >= B:
        break
print(sum(lst[A-1:B]))