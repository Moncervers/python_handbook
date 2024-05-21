price = float(input())

sum = 0.0

while price != 0:

    if price >= 500:
        sum += price * 0.9
    else:
        sum += price

    price = float(input())

print(sum)
