SCORE = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3,
}


def _get_game_result(choice1, choice2):
    if SCORE.get(choice1, 0) == SCORE.get(choice2, 0):
        return 3

    elif choice1 == "A":
        if choice2 == "Y":
            return 6
        else:
            return 0
    elif choice1 == "B":
        if choice2 == "Z":
            return 6
        else:
            return 0
    elif choice1 == "C":
        if choice2 == "X":
            return 6
        else:
            return 0


with open("input.txt", "r") as f:

    # Do something here
    content = f.read().splitlines()
    games = [line.split() for line in content]

    score = 0

    for choice1, choice2 in games:
        shape_score = SCORE.get(choice2, 0)
        game_score = _get_game_result(choice1, choice2)
        print(f"{choice1} {choice2} - Game score : {shape_score + game_score}")
        score += shape_score + game_score

    print(score)
