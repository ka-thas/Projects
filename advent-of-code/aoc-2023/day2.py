games = {}

def part2():
    # Orginalt dette jeg gjorde som del 1, men var for mye
    with open("inputs/day2.txt") as f:
        for line in f:
            line = line.strip()
            game_nr, blocks = line.split(":")
            game_nr = int(game_nr.split()[1])
            rounds = blocks.split(";")
            red = 0
            green = 0
            blue = 0
            for round in rounds:
                round = round.split(",")
                round = [x.strip().split() for x in round]
                for color in round:
                    if color[1] == "red" and int(color[0]) > red:
                        red = int(color[0])
                    if color[1] == "green" and int(color[0]) > green:
                        green = int(color[0])
                    if color[1] == "blue" and int(color[0]) > blue:
                        blue = int(color[0])
            games[game_nr] = [red, green, blue]

    sum = 0
    for i in games:
        power = games[i][0] * games[i][1] * games[i][2]
        sum += power
    print(sum)


def part1():
    sum = 0
    with open("inputs/day2.txt") as f:
        for line in f:
            line = line.strip()
            game_nr, blocks = line.split(":")
            game_nr = int(game_nr.split()[1]) 
            rounds = blocks.split(";")
            add = True
            for round in rounds:
                round = round.split(",")
                round = [x.strip().split() for x in round]
                for color in round:
                    if color[1] == "red" and int(color[0]) > 12:
                        add = False
                        break
                    if color[1] == "green" and int(color[0]) > 13:
                        add = False
                        break
                    if color[1] == "blue" and int(color[0]) > 14:
                        add = False
                        break
                if not add: break
            if add:
                sum += game_nr
    print(sum)

part2()

