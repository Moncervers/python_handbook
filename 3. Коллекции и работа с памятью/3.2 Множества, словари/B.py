first_line = set(input())
second_line = set(input())
lines_intersection = first_line.intersection(second_line)

for letter in lines_intersection:
    print(letter, end='')
