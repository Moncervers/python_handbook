n1 = int(input())
n2 = int(input())
p = 1
n3 = 0
for i in range(3):
    n3 += (n1 + n2) % 10 * p
    p *= 10
    n1 //= 10
    n2 //= 10
print(n3)