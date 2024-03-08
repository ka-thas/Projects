total = 0
lines = []
with open("inputs/day4.txt") as f:
    for line in f:
        line = line.split(":")
        line.append(None)
        drawn_nums, winning_nums = line[1].split("|")
        drawn_nums = drawn_nums.strip().split()
        winning_nums = winning_nums.strip().split()
        lines.append([1, drawn_nums, winning_nums])

for line_nr in range(len(lines)):
    current_num_vouchers = lines[line_nr][0]
    total += current_num_vouchers

    drawn_nums = lines[line_nr][1]
    temp_score = 0
    for drawn_num in drawn_nums:
        winning_nums = lines[line_nr][2]
        if drawn_num in winning_nums:
            temp_score += 1

    for modifier in range(1, temp_score +1):
        lines[line_nr + modifier][0] += current_num_vouchers


print(total)
