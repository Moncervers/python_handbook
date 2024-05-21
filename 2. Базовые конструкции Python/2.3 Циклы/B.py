str = input()
count = 0

while str != 'Приехали!':
    if 'зайка' in str:
        count += 1
    str = input()

print(count)