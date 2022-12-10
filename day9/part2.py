# def _debug_print_map(H, T):
#     map = [["." for x in range(0, 6)] for y in range(0, 6)]
#     map[H[0]][H[1]] = "H"

#     for idx, t in enumerate(T):
#         print(idx + 1, t)
#         map[t[0]][t[1]] = f"{idx+1}"

#     for line in map:
#         print(line)

#     print("\n")


with open("input.txt", "r") as f:
    content = f.read().splitlines()

instruction = [line.split(" ") for line in content]

visited_positions = set()  # We start at (0, 0), alwaty visited
H = (0, 0)
T = [(0, 0)] * 9
distance = 0


for dir, count in instruction:
    count = int(count)
    for i in range(count):
        if dir == "U":
            H = (H[0] + 1, H[1])
        elif dir == "D":
            H = (H[0] - 1, H[1])
        elif dir == "R":
            H = (H[0], H[1] + 1)
        elif dir == "L":
            H = (H[0], H[1] - 1)

        for i in range(9):
            # We define who we need to follow
            current_master = H if i == 0 else T[i - 1]

            distance_x = abs(current_master[0] - T[i][0])
            distance_y = abs(current_master[1] - T[i][1])

            icr_x = -1 if current_master[0] - T[i][0] > 0 else 1
            icr_y = -1 if current_master[1] - T[i][1] > 0 else 1

            if distance_x > 1:
                # They are on the same line, we need to update T
                T[i] = (current_master[0] + icr_x, T[i][1])
                if distance_y == 1:
                    # They are on the same column, we need to update T
                    T[i] = (T[i][0], current_master[1])
                elif distance_y > 1:
                    T[i] = (T[i][0], current_master[1] + icr_y)
            elif distance_y > 1:
                # They are on the same column, we need to update T
                T[i] = (T[i][0], current_master[1] + icr_y)
                if distance_x == 1:
                    # They are on the same line, we need to update T
                    T[i] = (current_master[0], T[i][1])
                elif distance_x > 1:
                    T[i] = (current_master[0] + icr_x, T[i][1])

        visited_positions.add((T[len(T) - 1][0], T[len(T) - 1][1]))

print(len(visited_positions))
