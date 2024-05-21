num_list = list(input())

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
num_list.sort()

if num_list[0] == 0:
    num_list[0], num_list[1] = num_list[1], num_list[0]
    print(f'{str(num_list[0]) + str(num_list[1])} {str(num_list[2]) + str(num_list[0])}')
    exit()

print(f'{str(num_list[0]) + str(num_list[1])} {str(num_list[2]) + str(num_list[1])}')

# Вообще, это должно решаться через кучу if, но я не собираюсь писать кучу условий