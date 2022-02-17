import sys; sys.stdin = open('2798.txt', 'r')

n, m = map(int, input().split())
num = list(map(int, input().split()))
len_n = len(num)
lst = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if num[i] + num[j] + num[k] <= m:
                lst.append(num[i] + num[j] + num[k])

max_v = 0
for i in lst:
    if i >= max_v:
        max_v = i

print(max_v)