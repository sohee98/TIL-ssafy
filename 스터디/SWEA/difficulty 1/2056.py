T = int(input())
for i in range(1, T + 1):
    date = input()
    if int(date[4:6]) in (1, 3, 5, 7, 8, 10, 12):
        if int(date[6:8]) <= 31:
            print(f'#{i} {date[0:4]}/{date[4:6]}/{date[6:8]}')
        else:
            print(f'#{i} -1')
    elif int(date[4:6]) in (4, 6, 9, 11):
        if int(date[6:8]) <= 30:
            print(f'#{i} {date[0:4]}/{date[4:6]}/{date[6:8]}')
        else:
            print(f'#{i} -1')
    elif int(date[4:6]) == 2:
        if int(date[6:8]) <= 28:
            print(f'#{i} {date[0:4]}/{date[4:6]}/{date[6:8]}')
        else:
            print(f'#{i} -1')
    else:
        print(f'#{i} -1')




        



