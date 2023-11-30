from sys import stdin

for i in stdin:
    name = ""
    prev_letter = ""
    for letter in i:
        if letter != prev_letter:
            name += letter
        prev_letter = letter
    print(name)
