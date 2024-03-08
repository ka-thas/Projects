total = 0
maps = {}
seeds = []
with open("inputs/day5.txt") as f:
    seeds = f.readline().strip().split()[1:]
    seeds = [int(x) for x in seeds]
    from_to = -1
    for line in f:
        line = line.strip()

        if not line:
            continue

        if ":" in line:
            from_to += 1
            maps[from_to] = []
            continue

        line = line.split()
        line = [int(x) for x in line]
        line[0] = line[0] - line[1]
        line[2] = line[1] + line[2]
        maps[from_to].append(line)

print("===========================================")

# Creating seed ranges
seed_ranges = []
for i, seed in enumerate(seeds[::2]):
    seed_ranges.append((seed, seed + seeds[i * 2 + 1]))


def remap(seed_range, map_range):
    a, b = seed_range
    shift, i, j = map_range
    new_seed_ranges = []

    # Ingen overlapp
    if b <= i or j <= a:
        return None

    if a < i:
        new_seed_ranges.append((a, i))

    snitt_start = max(a, i) + shift
    snitt_slutt = min(b, j) + shift
    new_seed_ranges.append((snitt_start, snitt_slutt))
    if j < b:
        new_seed_ranges.append((j, b))

    print(
        seed_range,
        map_range,
        new_seed_ranges,
        sep="\n",
    )
    print()
    return new_seed_ranges


new_seed_ranges = []


def recursive(seed_range, level):
    if level == 7:
        return [seed_range]

    for map_range in maps[level]:
        split_range = remap(seed_range, map_range)
        if split_range:
            print("---")
            break

    if not split_range:
        split_range = [seed_range]

    final_seed_ranges = []
    for seeds in split_range:
        new_partitions = recursive(seeds, level + 1)
        final_seed_ranges.extend(new_partitions)

    return final_seed_ranges


# TODO Noe rart når flere starseeds er i seedranges
seeds = []
for seed_range in seed_ranges:
    seeds.extend(recursive(seed_range, 0))
    print("ONE PATH DOWN")


seeds = [x[0] for x in seed_ranges]

print(seeds)

print(min(seeds))
