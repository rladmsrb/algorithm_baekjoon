import sys; sys.stdin = open('1209.txt')

for i in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0

    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]

        if total > max_v:
            max_v = total

    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[j][i]

        if total > max_v:
            max_v = total

    for i in range(100):
        total = 0
        total += arr[i][i]

    if total > max_v:
        max_v = total

    for i in range(100):
        total = 0
        total += arr[i][99-i]

    if total > max_v:
        max_v = total

    #  대각선 구하기
    '''
    
    dia1_sum = 0
    dia2_sum = 0
    
    for i in range(100):
        for j in range(100):
            if i == j:
                dia1_sum += arr[i][j]
            
            if i + j == 99:
                dia2_sum += arr[i][j]
    
    max_v = max_v if max_v > dia1_sum else dia1_sum
    max_v = max_v if max_v > dia2_sum else dia2_sum
    
    '''


    print(f'#{tc} {max_v}')