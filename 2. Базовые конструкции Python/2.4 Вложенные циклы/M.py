# TODO можно улучшить алгоритм
rows, cols = int(input()), int(input())
width = len(str(rows * cols))

counter = 1
for i in range(1, rows + 1):
    counter = i

    for j in range(1, cols + 1):
        # print(counter, end=' ')
        print(str(counter).rjust(width, ' '), end=' ')
        counter += rows
    print()
