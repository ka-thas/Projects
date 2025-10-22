tot, num_inputs = [int(x) for x in input().split(" ")]

mario = set()

for i in range(num_inputs):
    mario.add(int(input()))

for i in range(tot):
    if i not in mario:
        print(i)

print(f"Mario got {num_inputs} of the dangerous obstacles.")