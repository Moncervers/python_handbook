result = [0, 0]

while (direction := input()) != 'СТОП':
    step = int(input())

    match direction:
        case 'СЕВЕР':
            result[0] += step
        case 'ЮГ':
            result[0] -= step
        case 'ЗАПАД':
            result[1] -= step
        case 'ВОСТОК':
            result[1] += step

print(result[0])
print(result[1])
