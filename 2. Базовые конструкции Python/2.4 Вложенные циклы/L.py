rows, cols = int(input()), int(input())
width = len(str(rows * cols))
for i in range(1, rows + 1):
    for j in range(cols * (i - 1) + 1, cols * i + 1):
        if j == cols * i:
            print(str(j).rjust(width, ' '))
        else:
            print(str(j).rjust(width, ' '), end=' ')