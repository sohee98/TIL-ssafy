import sys
sys.stdin = open(f'1231input.txt', "r")
T = int(input())
for t in range(1, T+1):
     N, M, K = map(int, input().split())     # N명 M초 K개의 붕어빵
     guest = list(map(int, input().split())) # N개
     guest.sort()
     res = "Possible"
     for i in range(N):
          total = (guest[i]//M) * K
          if total < (i+1):
               res = "Impossible"
               break

     print('#{} {}'.format(t, res))


