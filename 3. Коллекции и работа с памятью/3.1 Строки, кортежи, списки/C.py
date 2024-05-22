str_lenght = int(input())
articles_amount = int(input())

for i in range(articles_amount):
    line = input()
    if len(line) > str_lenght:
        print(line[:str_lenght - 3], end='...\n')
    else:
        print(line)
