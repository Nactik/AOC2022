import numpy as np


with open("input.txt", "r") as f:
    content = f.read().splitlines()

max_scenic = 0
map = np.array([[int(x) for x in line] for line in content])

for x, line in enumerate(map):
    for y, tree in enumerate(line):
        # We get the trees in the 4 directions
        up = map[0:x, y]
        down = map[x + 1 :, y]
        left = map[x, 0:y]
        right = map[x, y + 1 :]

        # We apply the description of the problem word by word
        # For each direction, we count the number of trees until we find a
        # blocking one
        scenic_up, scenic_down, scenic_left, scenic_right = 0, 0, 0, 0
        for i in up[::-1]:
            if i < tree:
                scenic_up += 1
            else:
                scenic_up += 1
                break

        for i in down:
            if i < tree:
                scenic_down += 1
            else:
                scenic_down += 1
                break

        for i in left[::-1]:
            if i < tree:
                scenic_left += 1
            else:
                scenic_left += 1
                break

        for i in right:
            if i < tree:
                scenic_right += 1
            else:
                scenic_right += 1
                break

        scenic = scenic_up * scenic_down * scenic_left * scenic_right
        max_scenic = max(max_scenic, scenic)

print(max_scenic)
