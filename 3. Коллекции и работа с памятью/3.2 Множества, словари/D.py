oat_lovers, semolina_lovers = int(input()), int(input())
oat_lovers_set, semolina_lovers_set = set(), set()

for _ in range(oat_lovers):
    oat_lovers_set.add(input())
for _ in range(semolina_lovers):
    semolina_lovers_set.add(input())
if len(semolina_lovers_set & oat_lovers_set) == 0:
    print('Таких нет')
else:
    print(len(semolina_lovers_set & oat_lovers_set))