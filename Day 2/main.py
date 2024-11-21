with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

score = 0
master_list = []
new_list = []

for match in lines:
    new_list = []
    for char in match:
        if char == "A" or char == "X":
            new_list.append(1)
        elif char == "B" or char == "Y":
            new_list.append(2)
        elif char == "C" or char == "Z":
            new_list.append(3)
    master_list.append(new_list)

me = 0

for match in master_list:
    elf = match[0]
    result = match[1]
    if result == 2:
      me = elf
    if result == 1:
        if elf != 1:
            me = elf - 1
        elif elf == 1:
            me = 3
    if result == 3:
        if elf != 3:
            me = elf + 1
        elif elf == 3:
            me = 1
    if elf == 3 and me == 1:
        score += me + 6
    elif elf == 1 and me == 3:
        score += me
    elif elf < me:
        score += me + 6
    elif me < elf:
        score += me
    elif elf == me:
        score += me + 3

print(score)