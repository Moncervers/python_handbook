vpetya = int(input()) 
vvasya = int(input()) 
vtolya = int(input()) 
p = 'Петя'
v = 'Вася'
t = 'Толя'
m = ' '
if (vpetya > vvasya) and (vpetya > vtolya):
    if (vvasya > vtolya):
        print(f'{m * 10}{p}{m * 10}\n{m * 2}{v}{m * 2}\n{m * 18}{t}')
    else:
        print(f'{m * 10}{p}{m * 10}\n{m * 2}{t}{m * 2}\n{m * 18}{v}')
elif (vvasya > vpetya) and (vvasya > vtolya):
    if (vpetya > vtolya):
        print(f'{m * 10}{v}{m * 10}\n{m * 2}{p}{m * 2}\n{m * 18}{t}')
    else:
        print(f'{m * 10}{v}{m * 10}\n{m * 2}{t}{m * 2}\n{m * 18}{p}')
else:
    if (vpetya > vvasya):
        print(f'{m * 10}{t}{m * 10}\n{m * 2}{p}{m * 2}\n{m * 18}{v}')
    else:
        print(f'{m * 10}{t}{m * 10}\n{m * 2}{v}{m * 2}\n{m * 18}{p}')
print(f'{m * 3}II{m * 6}I{m * 6}III')