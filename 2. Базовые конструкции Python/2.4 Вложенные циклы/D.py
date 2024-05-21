sum = 0
num_count = int(input())

for i in range(num_count):
    num = input()
    for j in range(len(num)):
        sum += int(num[j])

print(sum)