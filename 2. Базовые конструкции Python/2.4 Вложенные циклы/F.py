count = int(input())
res = 0
num_list = []

first_num = int(input())

for i in range(count - 1):
    second_num = int(input())

    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num

    first_num = first_num + second_num

print(first_num)
