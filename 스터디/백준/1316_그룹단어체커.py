T = int(input())
cnt = 0
for tc in range(T):
    word = input()
    dic = {word[0]: 1}          # 첫번째 글자 추가
    for i in range(1, len(word)):   # 연속하지 않을 때 딕셔너리에 있으면 그룹단어가 아님
        if word[i] != word[i-1] and dic.get(word[i]):
            break
        dic[word[i]] = 1
    else:
        cnt += 1
print(cnt)