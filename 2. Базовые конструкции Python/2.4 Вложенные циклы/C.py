# for z in range(1, x := int(input()) + 1):
#     if z in (sum(range(i)) for i in range(x)):
#         print(z)
#     else:
#         print(z, end=' ')

num = int(input())
count = 0

for i in range(num):
    for j in range(i):
        print('*', end='')