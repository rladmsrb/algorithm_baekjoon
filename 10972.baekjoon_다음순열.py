# 순열함수를 구현하고
# if를 사용해서 마지막 값을 나타낼 땐 -1, 마지막 값이 아닐 땐 2번째 값을 도출하도록 한다.
# 풀이실패...

import sys; sys.stdin = open('10972.txt')

N = int(input())
A = list(map(int, input().split()))
visited = [0]*N  # 데이터의 사용 여부 - 데이터의 index 기록 ex)visited[1]=1
arr = [0]*N  # 어떤 데이터를 선택했는가 (순열 정보 저장) ex)arr[1]=2



def perm(level):
    if level >= N:
        print(arr)
        return

    for i in range(N):
        if visited[i] == 1:continue
        visited[i] = 1  # 사용표시(i인덱스에 있는 데이터 사용 중)
        arr[level] = A[i]
        perm(level+1)
        visited[i] = 0 # 사용해제

for i in perm(0):
    if A == [i][-1]:
        print(-1)

else:
    print([i][1])



