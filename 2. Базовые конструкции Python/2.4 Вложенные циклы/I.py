count = int(input())
max_digits_list = []

for i in range(count):
    temp = 0
    num = input()

    for digit in num:
        if int(digit) > temp:
            temp = int(digit)

    max_digits_list.append(temp)

for digit in max_digits_list:
    print(digit, end='')