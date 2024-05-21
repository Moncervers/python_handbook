one = str(input())
two = str(input())
three = str(input())
dl = 1000
mini = 'яяя'
if 'зайка' in one:
    mini = one
    dl = len(one)
if 'зайка' in two and two < mini:
    mini = two
    dl = len(two) 
if 'зайка' in three and three < mini:
    mini = three
    dl = len(three) 
print(f'{mini} {dl}') 