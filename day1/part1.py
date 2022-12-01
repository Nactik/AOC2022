with open('input.txt', "r") as f:
    # Do something here
    content = f.read().splitlines()
    inventory = []

    elf_id = 0
    sum = 0

    for line in content :
        if line == "":
            inventory.append(sum)
            sum=0
            elf_id += 1
        else:
            sum += int(line)

    print(max(inventory))