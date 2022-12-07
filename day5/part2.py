import re


with open("input.txt", "r") as f:

    header, content = f.read().split("\n\n")

    content_tab = content.splitlines()
    header_tab = header.splitlines()[:-1]

    # Failed attempt
    # fields = [re.split("    | ", line) for line in header_tab][:-1]

    stacks = []

    # We need to create stacks
    for line in header_tab:
        for idx, char in enumerate(re.split("    | ", line)):
            if idx > len(stacks) - 1:
                stacks.append([])
            if char != "":
                stacks[idx].append(char)

    actions = [
        re.search(r"move (\d+) from (\d+) to (\d+)", line).groups()
        for line in content_tab
    ]

    print(stacks)
    for count, source, target in actions:
        for i in range(int(count)):
            # Too lazy to reverse the stacks so we just pop the first element
            # and prepend it to the target stack
            stacks[int(target) - 1].insert(
                0, stacks[int(source) - 1].pop(int(count) - i - 1)
            )

    print(f"Final message: {''.join([x[0] for x in stacks])}")
