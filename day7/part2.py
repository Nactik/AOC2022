with open("input.txt", "r") as f:
    content = f.read().splitlines()

sizes = {}
previous_dir_stack = []
current_dir = ""

for line in content:
    print(previous_dir_stack, current_dir)
    if line.startswith("$"):
        _, cmd, *args = line.split(" ")
        if cmd == "cd":
            dir = args[0]
            if dir == "..":
                # If we go back, we get back the parent dir
                current_dir = previous_dir_stack.pop()
            elif dir == "/":
                # If we go to the root, we empty the stack
                current_dir = "/"
                previous_dir_stack = []

                if current_dir not in sizes:
                    sizes[current_dir] = 0
            else:
                # if we go deeper, we need to append
                # the current dir to the stack
                previous_dir_stack.append(current_dir)

                # Special case because my algo is bad af and didn't deal with
                # duplicate names, so I store the whole path:
                dir = "#".join([*previous_dir_stack, dir])

                current_dir = dir
                # We create the entry in the dict if it doesn't exist
                if current_dir not in sizes:
                    sizes[current_dir] = 0
    else:
        arg1, arg2 = line.split(" ")
        if arg1 != "dir":
            # We need to the size of the file to the current dir
            sizes[current_dir] += int(arg1)
            # We need to add the size of the file every parent dir as well
            for parent_dir in previous_dir_stack:
                sizes[parent_dir] += int(arg1)

total_used_size = sizes.get("/", 70000000)
unused_size = 70000000 - total_used_size
need_to_free = 30000000 - unused_size

filtered_sizes = [size for _, size in sizes.items() if size >= need_to_free]

# I need to sort
filtered_sizes.sort()

print(f"Size of the folder I should remove: {filtered_sizes[0]}")
