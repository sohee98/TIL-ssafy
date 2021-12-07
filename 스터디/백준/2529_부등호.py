## 참고함

k = int(input())
lst = list(input().split())
check = [0]*10

def compare(a, b, p):       # a, b를 비교한 결과 리턴
    if p == '<':
        return a < b
    if p == '>':
        return a > b

def solve(n, res):
    global maxV, minV
    if n == k+1:
        if not len(minV):   # 첫번째 값
            minV = res
        else:               # 마지막 값
            maxV = res
        return
    for i in range(10):
        if not check[i]:
            if n==0 or compare(res[-1], str(i), lst[n-1]):
                check[i] = 1
                solve(n+1, res+str(i))
                check[i] = 0

maxV = ""
minV = ""
solve(0, "")
print(maxV)
print(minV)