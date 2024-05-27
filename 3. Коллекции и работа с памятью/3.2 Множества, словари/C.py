new_set = set()

for _ in range(int(input())):
    for word in input().split():
        new_set.add(word)

for word in new_set:
    print(word)
