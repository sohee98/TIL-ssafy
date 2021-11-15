def solve(s):       # s : 총합
    global maxV
    if len(lst) == 2:
        if s > maxV:
            maxV = s
        return
    for i in range(1, len(lst)-1):
        tmp = lst[i]
        r = lst[i-1]*lst[i+1]
        lst.pop(i)      # 구슬 제거
        solve(s + r)    # 총합 + r
        lst.insert(i, tmp)  # 구슬 다시 넣기


N = int(input())
lst = list(map(int, input().split()))
maxV = 0
solve(0)
print(maxV)