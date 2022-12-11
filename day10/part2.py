with open("input.txt", "r") as f:
    content = f.read().splitlines()

instructions = [
    line.split(" ") if len(line.split(" ")) > 1 else [line, 0]
    for line in content
]

X = 1
cycle = 1
nvalues = []
CRT = [["_" for i in range(40)] for y in range(6)]

for opcode, value in instructions:
    to_cycle = 1
    if opcode == "addx":
        to_cycle = 2
    elif opcode == "noop":
        to_cycle = 1

    for i in range(0, to_cycle):
        # We need to draw if the sprite position overlaps our column (== cycle)
        # It overlaps if the center X is just after the column or just before
        # since the sprite is 3 pxl large
        idx_col = cycle - 1
        CRT[idx_col // 40][idx_col % 40] = (
            "#" if abs(X - (idx_col % 40)) <= 1 else "."
        )

        cycle += 1
        if i == to_cycle - 1:
            X += int(value)
        if cycle % 40 == 20:
            print(cycle, X)
            nvalues.append(X * cycle)

for line in CRT:
    print(line)
