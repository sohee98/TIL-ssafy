hour , minute = map(int, input().split())
if hour >= 0 and minute >= 45:
    print(f'{hour} {minute-45}')
elif hour == 0 and minute < 45:
    print(f'23 {15+minute)}')
else:
    print(f'{hour} {15+minute)}')