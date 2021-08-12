## 순차검색
# 정렬되어 있지 않은 경우
def sequentialSearch(key, lst):
    idx = 0
    N = len(lst)
    while idx < N and key != lst[idx]:
        idx += 1
    if idx == N:
        return -1
    return idx

lst = [4, 9, 11, 23, 2, 19, 7]
print(sequentialSearch(2, lst))
print(sequentialSearch(8, lst))
print(sequentialSearch(4, lst))         # 경계테스트
print(sequentialSearch(7, lst))
print('=================================')

# 정렬되어 있는 경우
def sequentialSearch2(key, lst):
    idx = 0
    N = len(lst)
    while idx < N and key > lst[idx]:
        idx += 1
    if idx < N and key == lst[idx]:
        return idx
    else:
        return -1

lst = [2, 4, 7, 9, 11, 19, 23]
print(sequentialSearch(7, lst))
print(sequentialSearch(1, lst))
print(sequentialSearch(2, lst))
print(sequentialSearch(5, lst))
print(sequentialSearch(23, lst))
print(sequentialSearch(30, lst))
print('=================================')

## 이진검색
def binaryS(key, lst):
    start = 0
    end = len(lst)-1
    while start <= end:
        m = (start+end)//2
        if key == lst[m]:
            return m
        elif key < lst[m]:
            end = m-1
        else:
            start = m+1
    return -1

lst = [2, 4, 7, 9, 11, 19, 23]
print(binaryS(7, lst))
print(binaryS(2, lst))
print(binaryS(23, lst))
print(binaryS(5, lst))
print(binaryS(1, lst))
print(binaryS(25, lst))
print('=================================')


## 선택 정렬
def selectionS(lst):
    N = len(lst)
    for i in range(N-1):
        # minV = lst[i]
        minP = i
        for j in range(i+1, N):
            if lst[minP] > lst[j]:      # minV > lst[i]:
                # minV = lst[j]
                minP = j
        lst[minP], lst[i] = lst[i], lst[minP]


lst = [4, 9, 11, 23, 2, 19, 7]
selectionS(lst)
print(lst)
print('=================================')






