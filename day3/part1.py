with open("input.txt", "r") as f:

    content = f.read().splitlines()

    # Do something here
    items = [
        [line[: len(line) // 2], line[len(line) // 2 :]] for line in content
    ]

    total = 0

    for items1, items2 in items:
        # Find common letter
        common = [letter for letter in items1 if letter in items2][0]

        priority = ord(common) - 96 if common.islower() else ord(common) - 38
        total += priority

    print(f"Total : {total}")
