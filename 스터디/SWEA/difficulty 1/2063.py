N = int(input())
num = list(map(int, input().split()))
num.sort()
print(num[N//2])