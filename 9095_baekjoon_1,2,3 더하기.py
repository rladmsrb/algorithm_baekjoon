import sys ; sys.stdin = open('9095.txt')

T = int(input())

# 규칙을 찾고 함수로 만들기!

def a(T):
    if T == 1:
        return 1
    if T == 2:
        return 2
    if T == 3:
        return 4
    else:
        return a(T-1) + a(T-2) + a(T-3)


for i in range(T):
    result = int(input())
    print(a(result))
