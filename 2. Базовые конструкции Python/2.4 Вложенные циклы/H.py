count = int(input())
max = 0
temp = 0
winner_name = ''

for i in range(count):
    name = input()
    num = input()
    temp = 0

    for digit in num:
        temp += int(digit)

    if temp >= max:
        max = temp
        winner_name = name

print(winner_name)
