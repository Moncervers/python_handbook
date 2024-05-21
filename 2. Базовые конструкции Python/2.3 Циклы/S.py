# Бинарный поиск
max_num = 1001
min_num = 1
res = (max_num - min_num) // 2
print(res)

while (str := input()) != 'Угадал!':

    match str:
        case 'Меньше':
            max_num = res

        case 'Больше':
            min_num = res

    res = (max_num + min_num) // 2

    print(res)