a = int(input())
b = int(input())
if a < b:
    while a != b + 1:
        print(a, end=' ')
        a += 1
else:
    while a != b - 1:
        print(a, end=' ')
        a -= 1