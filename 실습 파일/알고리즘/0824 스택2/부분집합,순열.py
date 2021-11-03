## 부분집합 구하기 - powerset
a = [28, 31, 78]
t = [False] * 3
def powerset(k):
    if k==3:
        print(t)                        # [True, True, True]
    else:
        t[k] = True
        powerset(k+1)
        t[k] = False
        powerset(k+1)
# powerset(0)

def powerset(k):
    if k==3:
        # print(t)
        for i in range(3):
            if t[i]:
                print(a[i], end=' ')
        print()                         # [28, 31, 78]
    else:
        t[k] = True
        powerset(k+1)
        t[k] = False
        powerset(k+1)
# powerset(0)

def powerset(k):
    if k==3:
        # print(t)
        for i in range(3):
            if t[i]:
                print(a[i], end=' ')
        print()
    else:
        for i in range(2):
            t[k] = i
            powerset(k+1)

# 부분집합 합이 10일 때
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def powerset(k, N, sumV):
    if sumV > 10:
        return
    if k==N:
        if sumV == 10:
            for i in range(N):
                if t[i]:
                    print(a[i], end=' ')
            print()
    else:
        t[k] = True
        powerset(k+1, N, sumV+a[k])
        t[k] = False
        powerset(k+1, N, sumV)

powerset(0, 10, 0)

## 순열
visited = [False] * 3
def per(k):
    if k==3:
        for i in range(3):
            print(a[t[i]], end=' ')
        print()
    else:
        for i in range(3):
            if not visited[i]:
                t[k] = i
                visited[i] = True
                per(k+1)
                visited[i] = False

a = [20, 31, 78]
t = [-1] * 3
# 0, 1, 2 => 20, 31, 78
# 0, 2, 1 => 20, 78, 31
# 1, 0, 2 => 31, 20, 78
# ...
per(0)


