# 로또 번호 6개 추첨하는 코드 작성하기
import random
numbers = range(1,46)
pick = random.sample(numbers,6)
print(pick)
