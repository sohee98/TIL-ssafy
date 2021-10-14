# 못품
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]   # 1:안타 2:2루타, 3:3루타, 4:홈런, 0:아웃

def play(lst):      # lst:타자 결과 리스트
    out = 0
    score = 0
    ground = [0, 0, 0, 0, 0, 0, 0]      # g[0]:1루, g[1]:2루, g[2]:3루, g[3:]:홈
    i = 0
    while out < 3:
        p = lst[i]  # 타자의 결과
        if p == 0:  # 아웃
            out += 1
        else:
            # p개씩 움직임
            ground[p-1], ground[p], ground[1+p], ground[2+p] = 1, ground[0], ground[1], ground[2]
            score += sum(ground[3:])
            ground[3:] = [0, 0, 0, 0]   # 홈 초기화
            i += 1

    return score

result = 0
for i in range(N):
    # 1번선수 빼고, 0인 선수를 뒤로 배치하고, 나머지 선수들을 오름차순으로 정렬
    player = arr[i][1:]     # 1번 선수 빼고
    r = []
    for p in player:
        if p:
            r.append(p)
    r.sort()                    # 0이 아닌 선수만 저장
    r.extend([0]*(9-len(r)))    # 0인 선수 추가
    r.insert(3, arr[i][0])      # 1번 선수는 4번에 고정
    print(r)

    result += play(r)
print(result)