from collections import deque

with open("input10.txt") as f:
    grid = []
    for i in f:
        row = []
        grid.append(row)
        for j in i.strip():
            row.append(int(j))

ROWS = len(grid)
COLS = len(grid[0])

trailheads = []
for i, row in enumerate(grid):
    print(row)
    for j, col in enumerate(row):
        if col == 0:
            trailheads.append((i, j))

print(trailheads)

sum = 0
for trailhead in trailheads:
    print()
    queue = deque([trailhead])
    visited = set()
    peaks = []  # Change to set for part 1!
    while queue:
        print(queue)
        node = queue.popleft()  # from the front
        visited.add(node)

        neighbors = [
            (node[0] - 1, node[1]),  # up
            (node[0] + 1, node[1]),  # down
            (node[0], node[1] - 1),  # left
            (node[0], node[1] + 1),  # right
        ]

        for j in neighbors:
            if j in visited:
                print(j, "already visited")
                continue
            elif j[0] < 0 or j[0] >= ROWS or j[1] < 0 or j[1] >= COLS:  # invalid coords
                print(j, "invalid coords")
                continue
            elif grid[j[0]][j[1]] != grid[node[0]][node[1]] + 1:  # invalid increment
                print(j, "invalid increment")
                continue
            elif grid[j[0]][j[1]] == 9:  # peak
                print(j, "found peak")
                peaks.append(j)
                continue
            queue.append(j)
            print(node, "->", j)
    print(len(peaks))
    print(peaks)
    sum += len(peaks)
print(sum)
