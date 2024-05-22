chars = ["А", "Б", "В"]
result = 'YES'

count = int(input())
for i in range(count):
    word = input()
    if word[0].upper() not in chars:
        result = 'NO'

print(result)

# for _ in range(int(input())):
#     if (word := input())[0] not in 'абв':
#         print('NO')
#         break
# else:
#     print('YES')