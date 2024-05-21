vpetya = int(input())
vvasya = int(input())
vtolya = int(input())

p = 'Петя'
v = 'Вася'
t = 'Толя'
if (vpetya > vvasya) and (vpetya > vtolya):
    if vvasya > vtolya:
        print(f'1. {p}\n2. {v}\n3. {t}')
    else:
        print(f'1. {p}\n2. {t}\n3. {v}')
elif (vvasya > vpetya) and (vvasya > vtolya):
    if vpetya > vtolya:
        print(f'1. {v}\n2. {p}\n3. {t}')
    else:
        print(f'1. {v}\n2. {t}\n3. {p}')
else:
    if vpetya > vvasya:
        print(f'1. {t}\n2. {p}\n3. {v}')
    else:
        print(f'1. {t}\n2. {v}\n3. {p}')