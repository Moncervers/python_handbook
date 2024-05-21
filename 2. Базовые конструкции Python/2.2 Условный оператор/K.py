num = input()

# first_digit = int(num[0])
# second_digit = int(num[1])
# third_digit = int(num[2])

min_digit = min(int(num[0]), int(num[1]), int(num[2]))
max_digit = max(int(num[0]), int(num[1]), int(num[2]))

num = num.replace(str(min_digit), '')
num = num.replace(str(max_digit), '')
if (max_digit + min_digit) == (int(num) * 2):
    print('YES')
else:
    print('NO')

# Решение, которое прошло
# n = int(input())
# a = n % 10
# b = n // 10 % 10
# c = n // 100 % 10
# if a >= b and a >= c:
#     maxi = a
#     if b >= c:
#         mini = c
#         sred = b
#     else:
#         mini = b
#         sred = c
# elif b >= a and b >= c:
#     maxi = b
#     if a >= c:
#         mini = c
#         sred = a
#     else:
#         mini = a
#         sred = c
# else:
#     maxi = c
#     if b >= a:
#         mini = a
#         sred = b
#     else:
#         mini = b
#         sred = a
#
# if maxi + mini == (sred * 2):
#     print('YES')
# else:
#     print('NO')