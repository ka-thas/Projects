grid = []
nums = [str(x) for x in range(10)]
chars = ["*", "$", "/", "+", "-", "=", "&", "#", "@", "%"]
tot = 0

with open("inputs/day3.txt") as f:
    for line in f:
        line = line.strip()
        grid.append(line)


def get_char(y, x):
    # Sjekk trygg kordinat
    if y >= len(grid) or x >= len(grid[0]) or y < 0 or x < 0:
        return None

    return grid[y][x]


def check_num_neighbors(y, x, len):
    for i in range(len):
        for y2 in range(-1, 2):
            for x2 in range(-1, 2):
                x2 += i
                if get_char(y + y2, x + x2) in chars:
                    return True
    return False


def find_star_neighbors(y, x):
    neighbors = []
    for y2 in range(-1, 2):
        for x2 in range(-1, 2):
            num = get_char(y + y2, x + x2)
            if num in nums:
                num = iterative_find_num(y + y2, x + x2, num)
                if num not in neighbors:
                    neighbors.append(num)
    return neighbors


def iterative_find_num(y, x, num):
    temp_x = x - 1
    left_num = get_char(y, temp_x)
    while left_num in nums:
        num = left_num + num
        temp_x -= 1
        left_num = get_char(y, temp_x)

    temp_x = x + 1
    right_num = get_char(y, x + 1)
    while right_num in nums:
        print("HEY!")
        num = num + right_num
        temp_x += 1
        right_num = get_char(y, temp_x)
    return int(num)


# PART 2
for y in range(len(grid)):
    for x in range(len(grid[0])):
        star = grid[y][x]
        if star != "*":
            continue

        star_stuff = find_star_neighbors(y, x)
        if len(star_stuff) == 2:
            tot += star_stuff[0] * star_stuff[1]


def part1():
    for y in range(len(grid)):
        skips = 0
        for x in range(len(grid[0])):
            if skips:
                skips -= 1
                continue

            num = grid[y][x]
            if num not in nums:
                continue

            next_char = get_char(y, x + 1)
            temp_x = x + 1
            while next_char in nums:
                num += next_char
                temp_x += 1
                next_char = get_char(y, temp_x)

            if check_num_neighbors(y, x, len(num)):
                tot += int(num)

            skips = len(num) - 1



print(tot)
