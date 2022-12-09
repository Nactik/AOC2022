def _debug_print_map(H, T):
    map = [["." for x in range(0, 6)] for y in range(0, 6)]
    map[H[0]][H[1]] = "H"
    for idx, t in enumerate(T):
        map[t[0]][t[1]] = f"{idx+1}"

    for line in map:
        print(line)

    print("\n")


with open("test.txt", "r") as f:
    content = f.read().splitlines()

instruction = [line.split(" ") for line in content]

visited_positions = set()  # We start at (0, 0), alwaty visited
H = (0, 0)
T = [(0, 0)] * 9
distance = 0
icr = [1] * 9


for dir, count in instruction:
    count = int(count)
    for i in range(count):
        icr[0] = 1  # Tells in wich direction we need to move T
        if dir == "U":
            H = (H[0] + 1, H[1])
            icr[0] = -1
        elif dir == "D":
            H = (H[0] - 1, H[1])
            icr[0] = 1
        elif dir == "R":
            H = (H[0], H[1] + 1)
            icr[0] = -1
        elif dir == "L":
            H = (H[0], H[1] - 1)
            icr[0] = 1

        for i in range(9):
            # We define who we need to follow

            current_master = H if i == 0 else T[i - 1]

            distance_x = abs(current_master[0] - T[i][0])
            distance_y = abs(current_master[1] - T[i][1])

            icrement = icr[i - 1] if i > 0 else icr[0]
            print(distance_x, distance_y, icrement)
            if distance_x > 1:
                # They are on the same line, we need to update T
                T[i] = (current_master[0] + icrement, T[i][1])
                icr[i] = icrement
                if distance_y == 1:
                    # They are on the same column, we need to update T
                    T[i] = (T[i][0], current_master[1])
            elif distance_y > 1:
                # They are on the same column, we need to update T
                T[i] = (T[i][0], current_master[1] + icrement)
                icr[i] = icrement
                if distance_x >= 1:
                    # They are on the same line, we need to update T
                    T[i] = (current_master[0], T[i][1])

        _debug_print_map(H, T)
        visited_positions.add((T[len(T) - 1][0], T[len(T) - 1][1]))

print(len(visited_positions))
