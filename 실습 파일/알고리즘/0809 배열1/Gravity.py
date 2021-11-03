# 1. 일차원배열에 높이를 넣는다 - 입력
# box = [7, 4, 2, 0, 0, 6, 0, 7, 0]
box = list(map(int, input().split()))

# 2. 각 열에서 우측에 자신의 높이보다 작은 열의 갯수를 센다.
    # i번쨰 열에서 i+1번째 열까지
maxV = 0
for i in range(len(box)):
    cnt = 0
    for j in range(i+1,len(box)):
        if box[i] > box[j]:
            cnt += 1

    # i번째 값이 현재까지 중에서 최대인지 비교하여 최대값을 maxV에 넣는다.
    if cnt > maxV:
        maxV = cnt

print(maxV)
