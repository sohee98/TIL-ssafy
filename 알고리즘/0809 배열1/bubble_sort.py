lst = [55, 7, 78, 12, 42]

N = 5
# 첫 번째 pass - N-1(4): 로 큰값을 N-1 위치로 보낸다.
    # 0-1, 1-2, 2-3, 3-4
# 두 번째 pass - N-2(3): 로 큰값을 N-2 위치로 보낸다.
    # 0-1, 1-2, 2-3
# i 번째 pass - N-i: 로 큰값을 N-2 위치로 보낸다.
    # 0-1, 1-2

for i in range(N-1, 0, -1):
    for j in range(0, i):
        # lst[i], lst[j+1]을 비교해서 lst[j] 크면 교환
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)