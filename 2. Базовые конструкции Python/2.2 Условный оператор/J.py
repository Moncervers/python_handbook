password = input()
first_digit = str(int(password[0]) + int(password[1]))
second_digit = str(int(password[1]) + int(password[2]))

if int(second_digit) > int(first_digit):
    print(second_digit + first_digit)
else:
    print(first_digit + second_digit)