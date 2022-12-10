with open("input.txt", "r") as f:
    content = f.read().splitlines()

instructions = [
    line.split(" ") if len(line.split(" ")) > 1 else [line, 0]
    for line in content
]

X = 1
cycle = 1
nvalues = []

for opcode, value in instructions:
    to_cycle = 1
    if opcode == "addx":
        to_cycle = 2
    elif opcode == "noop":
        to_cycle = 1

    for i in range(0, to_cycle):
        cycle += 1

        if i == to_cycle - 1:
            X += int(value)

        if cycle % 40 == 20:
            print(cycle, X)
            nvalues.append(X * cycle)

    print(opcode, value)

print(sum(nvalues))
