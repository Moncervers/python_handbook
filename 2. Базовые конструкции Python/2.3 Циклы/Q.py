num = input()
res = ''
for i in range(len(num)):
    if int(num[i]) % 2 == 1:
       res += num[i]

print(res)
