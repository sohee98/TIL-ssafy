# 원소의 합이 10인 부분집합 모두 출력
def prt():
    for i in range(N):
        if res[i] == 1:
            print(lst[i], end=' ')
    print()
    return

def powerset(k, sumV):
    if k == N:
        # sumV = 0
        # for i in range(N):
        #     if res[i] == 1:
        #         sumV += lst[i]
        if sumV == 10:
            prt()
        return

    res[k] = 0
    powerset(k+1, sumV)

    res[k] = 1
    powerset(k+1, sumV+lst[k])


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(lst)
res = [-1]*10
powerset(0, 0)


