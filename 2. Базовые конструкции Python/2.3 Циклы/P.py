num = input()

for i in range(len(num)//2):
    if num[i] != num[len(num)-i-1]:
        print('NO')
        exit()
print('YES')