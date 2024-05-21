username = input()
mood = input()

print('Как Вас зовут?')
print(f'Здравствуйте, {username}!')
print("Как дела?")
match mood:
    case 'хорошо':
        print("Я за вас рада!")
    case 'плохо':
        print("Всё наладится!")
