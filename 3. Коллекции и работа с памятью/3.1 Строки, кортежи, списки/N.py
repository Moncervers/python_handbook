num_list = list(map(int, input().split()))
power = int(input())

for num in num_list:
    print(num ** power, end=' ')
