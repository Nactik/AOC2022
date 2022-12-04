import re

with open("input.txt", "r") as f:

    content = f.read().splitlines()
    pairs = [re.split("-|,", line) for line in content]

    total = 0

    for low1, high1, low2, high2 in pairs:

        first_interval = range(int(low1), int(high1) + 1)
        second_interval = range(int(low2), int(high2) + 1)

        if int(low1) in second_interval or int(high1) in second_interval:
            total += 1
        elif int(low2) in first_interval or int(high2) in first_interval:
            total += 1

    print(f"Total : {total}")
