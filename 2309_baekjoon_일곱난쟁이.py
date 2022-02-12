import sys; sys.stdin = open('2309.txt')
N = 9
lst = []  # lst = [20, 7, 23, 19, 10, 15, 25, 8, 13]
for i in range(N):
    lst.append(int(sys.stdin.readline()))

# 난쟁이 키의 합 구하기

total = 0
for i in lst:
    total += i  # total = 140

# 총 합에서 2가지 인자를 뺐을 때 100이 나오는 상황

a = 0
b = 0
for i in lst:
    for j in lst:
        if total - i - j == 100:
            a = i
            b = j

'''
a = 0
b = 0
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if total - lst[i] - lst[j] == 100:
            a = lst[i]
            b = lst[j]
            
'''

lst.remove(a)
lst.remove(b) # lst = [20, 7, 23, 19, 10, 8, 13]

# 오름차순으로 정렬
for i in range(len(lst)-1,-1,-1):
    for j in range(0, i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]


for i in lst:
    print(i)





