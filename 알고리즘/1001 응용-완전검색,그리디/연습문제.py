## 1. 선택정렬 함수 - 재귀
def sortS(arr, k=0):
    minV = arr[k]
    minI = k
    for i in range(k+1, len(arr)):
        if arr[i] < minV:
            minV = arr[i]
            minI = i
    arr[k], arr[minI] = arr[minI], arr[k]
    # print(arr)
    if k+2 < len(arr):
        sortS(arr, k+1)
        return arr

arr = [3, 2, 9, 6, 7]
# print(sortS(arr))
# print(sortS([3, 6, 0, 8, 2, 1, 15, 4, 7, 9]))


## 2. 6자리 숫자 완전검색 적용 -> Baby-gin 검사
inp1 = '124783'
inp2 = '667767'
num = list(map(int,inp1.split()))


## 3. 부분집합의 합 