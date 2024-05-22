for i in range(int(input())):
    if 'зайка' in (line := input()):
        print(line.index('зайка') + 1)
    else:
        print('Заек нет =(')
