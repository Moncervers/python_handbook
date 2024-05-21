#пиздец, очень плохое решение, но самому писать лень
n = int(input())
namerez = 'Яяя'
for i in range(0, n):
    name = str(input())
    if namerez > name:
        namerez = name
print(namerez)