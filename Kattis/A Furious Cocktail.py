from sys import stdin

start = stdin.readline()
start = start.split()

potions = []
for i in stdin:
    potions.append(int(i))

potions.sort(reverse=True)

effects = []
out = "YES"
for i in range(len(potions)):
    effects.append(potions[i])
    for j in range(len(effects) - 1):
        effects[j] -= int(start[1])
        if effects[j] <= 0:
            out = "NO"
print(out)
