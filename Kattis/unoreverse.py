# WCFD

inp = input()
inp = inp.split(" ")
players = int(inp[0])
num_cards = int(inp[1])

players = [0 for i in range(players)]
# index 0 is me
# index 1 is the next player
# if only 0 has cards, then print yes
# anyone but 0 has cards, then print no
# if 0 and another has cards print maybe


def recursive(index, players, cards, høyre=True):
    if not cards:
        players[index] += 1
        return

    if index == 0:
        return

    for i in range(1, cards + 1):
        new_index = index
        new_dir = høyre

        if i % 2:  # odd
            new_dir = not new_dir

        if new_dir:
            new_index += 1
            if new_index == len(players):
                new_index = 0
        else:
            new_index -= 1
            if new_index == -1:
                new_index = len(players) - 1

        recursive(new_index, players, cards - i, new_dir)


recursive(1, players, num_cards)


if players[0] and any([p > 0 for p in players[1:]]):
    print("maybe")
elif players[0]:
    print("yes")
else:
    print("no")
