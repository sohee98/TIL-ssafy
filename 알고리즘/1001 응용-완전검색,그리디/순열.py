# 순열 - 재귀
def perm(n, k):     # n:원소의개수
    if k == n:
        print(p)
        return
    else:
        for i in range(k, n):
            p[k], p[i] = p[i], p[k]
            perm(n, k+1)
            p[k], p[i] = p[i], p[k]

p = [1, 2, 3]
# perm(3, 0)

# 사용여부에 따른 순열
def f(n, m, k):     # n:순열의 길이, k:결정할 위치
    if n == k:
        print(p)
    else:
        for i in range(m):      # 주어진 숫자의 개수만큼
            if u[i] == 0:
                u[i] = 1
                p[k] = arr[i]
                f(n, m, k+1)
                u[i] = 0

p = [0]*5
arr = [1, 2, 3, 4, 5]
u = [0]*5
# f(3, 5, 0)

# 첫번째 숫자 고정
p[0] = arr[0]
u[0] = 1
f(5, 5, 1)

