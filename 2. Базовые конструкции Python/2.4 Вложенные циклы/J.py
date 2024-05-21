count = int(input())

for i in range(1, count - 1):
    if i == 1:
        print('А Б В')
    for j in range(1, count - i):
        print(f'{i} {j} {count - i - j}')