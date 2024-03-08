total = 0
maps = {}
seeds = []
with open("inputs/day5.txt") as f:
    seeds = f.readline().strip().split()[1:]
    seeds = [int(x) for x in seeds]
    from_to = ""
    for line in f:
        line = line.strip()

        if not line:
            continue

        if ":" in line:
            from_to = line
            maps[from_to] = []
            continue

        line = line.split()
        line = [int(x) for x in line]
        line[0] = line[0] - line[1]
        maps[from_to].append(line)

print("===========================================")

val = None
locations = []
for i in seeds:
    print("\n=========")
    val = i
    for key in maps:
        for line in maps[key]:
            if val >= line[1] and val < line[1] + line[2]:
                val += line[0]
                print(i, key, val)
                break

    locations.append(val)
print(min(locations))
