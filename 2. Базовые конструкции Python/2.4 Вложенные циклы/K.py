count = 0
for i in range(int(input())):
    j = 2
    if (n := int(input())) > 1:
        count += 1
        if n == 2:
            count += 1
        while n % j:
            if j > n ** 0.5:
                break
            j += 1
        else:
            count -= 1
print(count)