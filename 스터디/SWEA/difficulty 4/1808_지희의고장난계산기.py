def makeNum(n, num_list):
    for i in range(len(lst)):
        for j in range(len(lst)):
            num_list.append(lst[i]*10 + lst[j])




T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    X = int(input())
    num = []
    for i in range(10):
        if lst[i]:
            num.append(i)
    print(num)
    i = 0
    num_list = list(num)
