num_list = []
for i in range(int(input())):
    num_list.append(int(input()))

power = int(input())
for num in num_list:
    print(num ** power)