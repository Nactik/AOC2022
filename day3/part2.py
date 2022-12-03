with open("input.txt", "r") as f:

    content = f.read().splitlines()

    # Do something here
    groups = [
        [content[i], content[i + 1], content[i + 2]]
        for i in range(0, len(content), 3)
    ]

    total = 0

    for items1, items2, items3 in groups:
        # Find common letter
        common = [
            letter
            for letter in items1
            if (letter in items2 and letter in items3)
        ][0]
        priority = priority = (
            ord(common) - 96 if common.islower() else ord(common) - 38
        )

        total += priority

    print(f"Total : {total}")
