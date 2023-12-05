total = 0
maps = {}
seeds = []
with open("inputs/day5.txt") as f:
    seeds = f.readline().strip().split()[1:]
    seeds = (int(x) for x in seeds)
    from_to = ""
    for line in f:
        line = line.strip()

        if not line:
            continue

        if ":" in line:
            from_to = line
            maps[from_to] = {}
            continue
        
        line = line.split()
        line = [int(x) for x in line]
        for i in range(line[2]):
            seed = line[1] + i
            soil = line[0] + i
            maps[from_to][seed] = soil

print("Done reading from file!")

val = None
locations = []
for i in seeds:
    val = i
    for map in maps:
        if val in maps[map].keys():
            val = maps[map][val]
    locations.append(val)
print(min(locations))