import numpy as np


with open("input.txt", "r") as f:
    content = f.read().splitlines()

count = 0

map = np.array([[int(x) for x in line] for line in content])

for x, line in enumerate(map):
    for y, tree in enumerate(line):
        # We get the trees in the 4 directions
        up = map[0:x, y]
        down = map[x + 1 :, y]
        left = map[x, 0:y]
        right = map[x, y + 1 :]

        # If my tree is the biggest in one of the 4 directions, I count it
        if (
            all(tree > up)
            or all(tree > down)
            or all(tree > left)
            or all(tree > right)
        ):
            count += 1

print(count)
