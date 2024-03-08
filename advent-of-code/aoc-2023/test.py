def old():
    s = "epleeple"
    s = s.replace("eple", "banan")
    print(s)

    s = " 2 green"
    print(s.strip())

    for i in range(-1, 2):
        print(i)

    chars = []
    with open("inputs/test.txt") as f:
        for i in f:
            i = i.strip()

            for j in i:
                if j not in chars:
                    chars.append(j)

    line = [50, 98, 2]
    print(line)
    for i in range(line[1], line[1] + line[2]):
        print(i)


# 5:2
with open("inputs/day5.txt") as f:
    seeds = f.readline().strip().split()[1:]
    seeds = [int(x) for x in seeds]

for i, seed in enumerate(seeds[::2]):
    print(i * 2, seed)
