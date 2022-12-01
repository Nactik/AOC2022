with open('input.txt', "r") as f:
    # Do something here
    content = f.read().splitlines()
    inventory = []

    elf_id = 0
    calories = 0

    for line in content :
        if line == "":
            inventory.append(calories)
            calories=0
            elf_id += 1
        else:
            calories += int(line)

    inventory.append(calories) ## Append last count

    inventory.sort(reverse=True) ## Sort the list
    top_three = inventory[:3] ## Get the top threes

    print(sum(top_three))