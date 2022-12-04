import re

with open("input.txt", "r") as f:

    content = f.read().splitlines()
    pairs = [re.split("-|,", line) for line in content]

    total = 0

    for low1, high1, low2, high2 in pairs:
        print(low1, high1, low2, high2)
        if int(low1) <= int(low2) and int(high1) >= int(high2):
            total += 1
        elif int(low2) <= int(low1) and int(high2) >= int(high1):
            total += 1

    print(f"Total : {total}")
