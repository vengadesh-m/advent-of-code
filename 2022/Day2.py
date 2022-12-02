import os

input = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEP = os.path.sep

file = f"{BASE_DIR}{SEP}sample_inputs{SEP}Day2.txt"

with open(file) as _file:
    for line in _file:
        input.append(tuple(line.strip("\n").split()))


rock = "rock"
paper = "paper"
scissor = "scissor"
rps_map = {'A': rock, 'B': paper, 'C': scissor, 'X': rock, 'Y': paper, 'Z': scissor}
score_map = {rock: 1, paper: 2, scissor: 3}
win_map = {rock: paper, paper: scissor, scissor: rock}
lose_map = {rock: scissor, scissor: paper, paper: rock}

def rps_result(opponent_value, your_value):
    lost = 0
    draw = 3
    win = 6
    if opponent_value == your_value:
        return draw + score_map[your_value]

    if your_value != lose_map[opponent_value]:
        return win + score_map[your_value]
    else:
        return lost + score_map[your_value]

score_board = [rps_result(rps_map[opp], rps_map[you]) for opp, you in input]

print("Total score of Part 1 ", sum(score_board))

def decided_results(opponent_value, your_raw_value):
    decider_map = {'X': 'lost', 'Y': 'draw', 'Z': 'win'}
    if decider_map[your_raw_value] == 'lost':
        return score_map[lose_map[opponent_value]]
    if decider_map[your_raw_value] == 'win':
        return score_map[win_map[opponent_value]] + 6
    return score_map[opponent_value] + 3

round2_score_board = [decided_results(rps_map[opp], you) for opp, you in input]

print("Total score of Part 2 is ", sum(round2_score_board))
