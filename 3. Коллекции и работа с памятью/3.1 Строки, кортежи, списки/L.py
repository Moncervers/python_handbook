menue = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

for i in range(int(input())):
    print(menue[i % len(menue)])
