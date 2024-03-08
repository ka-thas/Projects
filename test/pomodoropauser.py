import random

my_list = []
inp = input("")
while inp:
    if inp == "pop":
        print(random.choice(my_list))

    elif inp == "push":
        with open("pomodoropauser.txt", "w") as f:
            for i in my_list:
                f.write(i + "\n")

    elif inp == "pull":
        with open("pomodoropauser.txt") as f:
            for line in f:
                my_list.append(line.strip())

    elif inp == "list":
        print(my_list)
        
    else:
        my_list.append(inp)
    inp = input("")
