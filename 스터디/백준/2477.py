# 1동 2서 3남 4북
K = int(input())
n_list = []
m_list = []
for _ in range(6):
    n, m = map(int, input().split())
    n_list.append(n)    # 방향 리스트
    m_list.append(m)    # 길이 리스트
n1 = []
n2 = []
for i in range(6):
    if n_list.count(n_list[i]) == 1:    # 방향이 한번만 나오는 길이 리스트
        n1.append(m_list[i])
    if n_list.count(n_list[i]) == 2:    # 방향이 두번 나오는 길이 리스트
        n2.append(m_list[i])
if n_list[0] == n_list[2] and n_list[1] == n_list[5]:
    area = n1[0]*n1[1] - n2[0]*n2[1]
elif n_list[0] == n_list[4] and n_list[1] == n_list[5]:
    area = n1[0]*n1[1] - n2[0]*n2[3]
elif n_list[0] == n_list[4] and n_list[5] == n_list[3]:
    area = n1[0]*n1[1] - n2[2]*n2[3]
else:
    area = n1[0]*n1[1] - n2[1]*n2[2]

result = area*K
print(result)
