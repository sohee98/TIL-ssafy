## 은성님 코드 참고

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p += t
q += t
a, b = divmod(p, w)     # p:원래 위치, w:격자 길이
c, d = divmod(q, h)     # a,c : 몫/ c,d: 나머지

if a % 2:   # 몫이 짝수면 나머지가 그래프에 있는 값
    p = w - b
else:
    p = b
if c % 2:
    q = h - d
else:
    q = d

print(p, q)


