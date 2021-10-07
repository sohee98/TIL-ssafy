A, B = input().split()
diff = len(B)-len(A)

minC = 50
for i in range(diff):   # 길이 차이만큼 반복
    cnt = 0
    for b in range(len(A)):
        if A[b] != B[b+i]:
            cnt += 1
    if cnt < minC:
        minC = cnt

print(minC)