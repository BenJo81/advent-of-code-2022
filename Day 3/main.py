with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

score = 0
master_list = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


# def split_string(string):
#     midpoint = len(string) // 2
#     first_half = string[:midpoint]
#     second_half = string[midpoint:]
#
#     return first_half, second_half


while len(lines) > 0:
    count = 0
    test_list = []
    master_list = []

    while count < 3:
        count += 1
        test_list.append(lines[0])
        lines.pop(0)

    print(test_list)

    for char in test_list[0]:
        if char in test_list[1] and char in test_list[2]:
            got_it = char
    master_list.append(got_it)

    print(master_list)

    for item in master_list:
        index = alphabet.index(item.lower())
        index += 1
        if item.islower():
            score += index
        elif item.isupper():
            score += (index + 26)

print(score)