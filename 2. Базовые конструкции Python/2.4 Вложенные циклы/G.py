racer_count = int(input())

for i in range(racer_count):
    for j in range(i + 3, 0, -1):
        print(f'До старта {j} секунд(ы)')

    print(f'Старт {i + 1}!!!')
