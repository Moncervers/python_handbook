# TODO можно улучшить алгоритм
unique_list = []
final_line, answer = '', ''
max_amount = 0

while (line := input()) != 'ФИНИШ':
    final_line += line.lower()

final_line = final_line.replace(' ', '')
unique_list = sorted(set(final_line))

for char in unique_list:
    if final_line.count(char) > max_amount:
        answer = char
        max_amount = final_line.count(char)

print(answer)

# Чужой алгоритм
# data = []
# while (n := input()) != 'ФИНИШ':
#     data.extend(n.lower().split())
# max_count, data = 0, ''.join(data)
# for symbol in set(data):
#     max_count = max(max_count, data.count(symbol))
# print(min([i for i in set(data) if data.count(i) == max_count]))
