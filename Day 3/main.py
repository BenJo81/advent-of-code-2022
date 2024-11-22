with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

score = 0
master_list = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def split_string(string):
    midpoint = len(string) // 2
    first_half = string[:midpoint]
    second_half = string[midpoint:]

    return first_half, second_half


for item in lines:
    part_1, part_2 = split_string(item)
    for char in part_1:
        if char in part_2:
            got_it = char
    master_list.append(got_it)

for item in master_list:
    index = alphabet.index(item.lower())
    index += 1
    if item.islower():
        score += index
    elif item.isupper():
        score += (index + 26)

print(score)