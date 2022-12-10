def _debug_print_map(H, T):
    map = [["." for x in range(0, 6)] for y in range(0, 6)]
    map[H[0]][H[1]] = "H"
    map[T[0]][T[1]] = "T"

    for line in map:
        print(line)

    print("\n")


with open("test.txt", "r") as f:
    content = f.read().splitlines()

instruction = [line.split(" ") for line in content]

visited_positions = set()  # We start at (0, 0), alwaty visited
H = (0, 0)
T = (0, 0)

for dir, count in instruction:
    count = int(count)
    for i in range(count):
        icr = 1  # Tells in wich direction we need to move T
        if dir == "U":
            H = (H[0] + 1, H[1])
            icr = -1
        elif dir == "D":
            H = (H[0] - 1, H[1])
            icr = 1
        elif dir == "R":
            H = (H[0], H[1] + 1)
            icr = -1
        elif dir == "L":
            H = (H[0], H[1] - 1)
            icr = 1

        distance_x = abs(H[0] - T[0])
        distance_y = abs(H[1] - T[1])

        if distance_x > 1:
            # They are on the same line, we need to update T
            T = (H[0] + icr, T[1])
            if distance_y == 1:
                # They are on the same column, we need to update T
                T = (T[0], H[1])
        elif distance_y > 1:
            # They are on the same column, we need to update T
            T = (T[0], H[1] + icr)
            if distance_x >= 1:
                # They are on the same line, we need to update T
                T = (H[0], T[1])

        _debug_print_map(H, T)
        visited_positions.add((T[0], T[1]))

print(len(visited_positions))
