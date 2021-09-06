word = input()
C = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
C1 = ['c', 'd', 'l', 'n', 's', 'z']
tmp = []
cnt = 0
for i in range(len(word)):
    if len(tmp) == 0:
        if word[i] not in C1 or i==len(word)-1:
            cnt += 1
        else:
            tmp += [word[i]]
        continue
    tmp += [word[i]]
    if len(tmp) == 2:
        if ''.join(tmp) in C:
            cnt += 1
            tmp = []
        elif ''.join(tmp) == 'dz':
            if i == len(word)-1:
                cnt += 2
                break
            elif word[i+1]=='=':
                tmp = []
            else:
                tmp.pop(0)
                cnt += 1
        else:
            tmp.pop(0)
            cnt += 1
    if i == len(word)-1:
        cnt += len(tmp)
print(cnt)







