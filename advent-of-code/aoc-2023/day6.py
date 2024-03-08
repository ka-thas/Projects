with open("inputs/day6.txt") as f:
    data = f.read()
time, distance = data.split("\n")
time = [int(x) for x in time.split()[1:]]
distance = [int(x) for x in distance.split()[1:]]


def part2(time, distance):
    time = time[0]
    distance = distance[0]

    for hold_button in range(time):
        if (time - hold_button) * hold_button > distance:
            min = hold_button
            print(min)
            break

    tot_wins = time - (2 * min) + 1

    print(tot_wins)


part2(time, distance)


def part1(time, distance):
    return_val = 0
    for i, race_time in enumerate(time):
        num_wins = 0
        for hold_button in range(race_time):
            speed = hold_button
            if (race_time - hold_button) * hold_button > distance[i]:
                num_wins += 1
        return_val = return_val * num_wins if return_val else num_wins
    print(return_val)


# part1(time, distance)
