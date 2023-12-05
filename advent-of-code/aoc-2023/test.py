s = "epleeple"
s = s.replace("eple", "banan")
print (s)

s = " 2 green"
print(s.strip())

for i in range(-1,2):
    print(i)

chars = []
with open("inputs/test.txt") as f:
    for i in f:
        i = i.strip()

        for j in i:
            if j not in chars:
                chars.append(j)
print(chars)