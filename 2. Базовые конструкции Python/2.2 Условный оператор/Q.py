a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c

if d < 0:
    print('No solution')
    exit()
if b == 0 and c == 0:
    print('Infinite solutions')
    exit()

result = [(-b + (d ** 0.5)) / (2 * a), (-b + -(d ** 0.5)) / (2 * a)]
result.sort()

if result[0] == result[1]:
    print(result[0])
    exit()

print(f'{result[0]:.2f}, {result[1]:.2f}')
