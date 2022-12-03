SCORE = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3, # Scissors
}

RESULT = {
    "X": 0, # Lose
    "Y": 3, # Draw
    "Z": 6, # Win
}


def _get_move_score(choice1: str, expected_result: int) -> int:

    if expected_result == 3: # Draw
        # print(f"{SCORE[choice1]} {result} - I should choose {SCORE.get(choice1, 0)}")
        return SCORE.get(choice1, 0)
  
    if expected_result == 0: # Lose
        # print(f"{SCORE[choice1]} {result} - I should choose {(SCORE.get(choice1, 0) + 2) % 3} ")
        return (SCORE.get(choice1, 0) + 1) % 3 + 1 
  
    # print(f"{SCORE[choice1]} {result} - I should choose {(SCORE.get(choice1, 0) + 1) % 3} ")
    return (SCORE.get(choice1, 0)) % 3 + 1


with open('input.txt', "r") as f:

    
    # Do something here
    content = f.read().splitlines()
    games = [line.split() for line in content]

    score = 0

    for choice1, expected_result in games:
        result = RESULT.get(expected_result, 0)
        move_score = _get_move_score(choice1, result)

        # print(f"{choice1} {result} - Game score : {move_score + result}")
        score += (move_score + result)
        
    print(f"Total score: {score}")