num = int(input())

count = 2
simple = True

if num <= 1:
    simple = False
else:
    while count <= num ** 0.5 and simple is True:
        if num % count == 0:
            simple = False
        else:
            count = count + 1

if simple is True:
    print('YES')
else:
    print('NO')