nums = [str(x) for x in range(1,10)]
num_words = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

with open("inputs/day1.txt") as f:
    total = 0
    for line in f:
        line = line.strip()
        num1 = None
        num2 = None

        for i in num_words: # Part 2
            if i in line:
                line = line.replace(i, num_words[i])

        for char in line:
            if char in nums:
                num1 = char if num1 is None else num1
                num2 = char
        line_num = int(num1 + num2)
        total += line_num
print(total)

