round_weight = {'X': 0, 'Y': 3, 'Z': 6}

choice_weight = {'A': 1, 'B': 2, 'C': 3}

game_conditions = {'A': 'B', 'B': 'C', 'C': 'A'}

games_score = 0


def read_file(filename):
    all_lines = []
    file1 = open(filename, "r")

    while True:
        line = file1.readline()
        if not line:
            break
        all_lines.append(line.strip().split(' '))

    file1.close
    return all_lines


def calculate_player_choice(opponent_choice, game_result):
    if game_result == 'Y':
        return opponent_choice
    elif game_result == 'Z':
        return game_conditions[opponent_choice]
    elif game_result == 'X':
        for key in game_conditions:
            if game_conditions[key] == opponent_choice:
                return key


for game_round in read_file("input_data.txt"):
    round_result = calculate_player_choice(*game_round)
    games_score += round_weight[game_round[1]] + choice_weight[round_result]

print('Total score:', games_score)
