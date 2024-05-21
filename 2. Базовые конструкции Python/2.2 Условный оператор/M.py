elf = input()
dwarf = input()
human = input()

elf_first = elf[0]
elf_second = elf[1]

dwarf_first = dwarf[0]
dwarf_second = dwarf[1]

human_first = human[0]
human_second = human[1]

# min_first_digit = min(elf_first, dwarf_first, human_first)
# max_first_digit = max(elf_first, dwarf_first, human_first)
#
# min_second_digit = min(elf_second, dwarf_second, human_second)
# max_second_digit = max(elf_second, dwarf_second, human_second)
#

if elf_first == dwarf_first == human_first:
    print(elf_first)
elif elf_second == dwarf_second == human_second:
    print(dwarf_second)
