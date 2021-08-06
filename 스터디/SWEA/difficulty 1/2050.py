al = list(input())
lst = []
for i in range(len(al)):
    lst.append(ord(al[i])-64)
print(*lst)

