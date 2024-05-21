first_num = list(input())
second_num = list(input())
num_list = first_num + second_num

min_num = min(num_list)
max_num = max(num_list)

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

temp = sum(num_list) - int(min_num) - int(max_num)

print(max_num + str(temp)[-1] + min_num)