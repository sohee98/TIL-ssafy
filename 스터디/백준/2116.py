## 못품 참고함
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

t = [-1] * n # 아래값 인덱스 위치저장리스트
target_lst = [-1] * n # target에 저장된 목표값 저장리스트
result = 0

for i in range(6):
    k = 0
    t[k] = i
    while k < n: # 지정된 k(k번째 주사위)의 아래값을 보고 위에 위치한 값을 찾아냄
        if t[k] == 0:
            target = lst[k][5]
        elif t[k] == 1:
            target = lst[k][3]
        elif t[k] == 2:
            target = lst[k][4]
        elif t[k] == 3:
            target = lst[k][1]
        elif t[k] == 4:
            target = lst[k][2]
        else:
            target = lst[k][0]
        target_lst[k] = target # 찾아낸 target을저장함
        if k < n-1: # 맨 위가 아닌 경우 다음 k+1번째 주사위의 아래인덱스를 찾아야함
            for j in range(6):
                if lst[k+1][j] == target:
                    t[k+1] = j
        k += 1
    total = 0  # 여러개의 주사위 눈의 합
    for r in range(n): # n개의 주사위의 에서 t[k]에 저장된 리스트의 인덱스값과 target_lst에 저장된 값에 해당이 안되는 수 중 가장 큰 값을 찾음
        for num in range(6,0,-1): #  주사위 큰수부터 내림차순으로 진행
            if (num != target_lst[r]) and (num != lst[r][t[r]]):
                total += num
                break  # 찾으면 다음칸으로 이동
    if total > result: # 모두 합한값이 다른 경우의 수보다 크면 result에 저장한다.
        result = total
print(result)