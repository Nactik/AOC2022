with open("input.txt", "r") as f:

    chars = [char for char in f.read().strip()]

    start_idx = 0
    for i in range(0, len(chars)):
        non_duplicate = set(chars[i : i + 4])
        if len(non_duplicate) == len(chars[i : i + 4]):
            start_idx = i + 4
            break

    print(f"Start of packet: {start_idx}")
