petya_speed = int(input())
vasya_speed = int(input())
vitaly_speed = int(input())

if max(petya_speed, vasya_speed, vitaly_speed) == petya_speed:
    print('Петя')
elif max(petya_speed, vasya_speed, vitaly_speed) == vasya_speed:
    print('Вася')
else:
    print('Толя')