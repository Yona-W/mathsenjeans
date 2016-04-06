import functions
import random
from copy import deepcopy

def do_turn(self, game, eval_functions, ignore_legality = False):
	game_state = deepcopy(game)
	#import ipdb;ipdb.set_trace()
	scores_per_move = [0, 0, 0, 0, 0, 0]
	for turn in range(0, 6):
		new_state = functions.play(game_state, turn, True)
		#print(new_state)
		if not new_state: 
			#print("skipping impossible turn")
			scores_per_move[turn] = -10000000.0
			continue
		#print("playing")

		if not deepcopy(new_state).is_state_legal(True) or ignore_legality:
			#import ipdb;ipdb.set_trace()
			scores_per_move[turn] = -10000000.0
			continue
		else:
			for function in eval_functions:
				#print("Calling function",function)
				scores_per_move[turn] += function(self, game_state, new_state, arthur_kms(new_state.stones))
	#import ipdb;ipdb.set_trace()
	best_score = max(scores_per_move)
	if best_score == -10000000.0:
		return random.randint(1, 7)
	#print(best_score)
	i = 0
	for score in scores_per_move:
		i += 1
		if score == best_score:
			#print(i)
			#print(game.stones)
			#print(scores_per_move, best_score, i)
			return i

def check_if_slot_capturable_by_enemy(board, slot):
    for enemy_slot in range(6, 12):
        slot_to_capture = (enemy_slot + board[enemy_slot] + board[enemy_slot] // 12) % 12
        if slot_to_capture == slot and 0 < board[slot_to_capture] < 3:
            return True
    return False

def check_if_slot_capturable_by_me(board, slot):
    for my_slot in range(0, 6):
        slot_to_capture = (my_slot + board[my_slot] + board[my_slot] // 12) % 12
        if slot_to_capture == slot and 0 < board[slot_to_capture] < 3:
            return True
    return False

# Above this line is pure coding magic, prepared by our great algomancer Jonathan Montineri.
# Below this line is pure math sorcery, prepared by our great spellcaster Arthur Schichl.

# (No, we have no clue how this program works, don't ask for too many details. At least, I hope it works.)

def arthur_g(x):
    if 0 <= x <= 0.25:
        return 1.0
    elif 0.25 <= x <= 0.75:
        return 8.0 * x - 1.0
    else:
        return -(1.0 / 5.0)

def arthur_h(x):
    if 0 <= x <= 0.25:
        return 1.0
    elif 0.25 <= x <= 0.5:
        return 16.0 * x - 3.0
    elif 0.5 <= x <= 0.75:
        return 20.0 * x - 5.0
    else:
        return 80.0 * x - 50.0

def arthur_i(x):
    if 0 <= x <= 0.65:
        return 1.0
    elif 0.65 <= x <= 0.75:
        return -5.0 * x + 4.25
    else:
        return 0.0

def arthur_j(x):
    if 0 <= x <= 0.25:
        return 0.4 * x + 0.1
    elif 0.25 <= x <= 0.5:
        return 3.2 * x - 0.6
    else:
        return 1.0

def arthur_k(board): #Because he's too cool for consistency in variables 8-)
    #import ipdb;ipdb.set_trace()
	average = float(sum(board)) / float(len(board))
	maximum = max(board)
	try:
		return (maximum / average) ** 2
	except Exception as e:
		#print(board)
		return 0


def arthur_m(x): #m stands for magic, i think
    if 0 <= x <= 40:
        #WHAT THE ACTUAL FUCK
        return 1.606e-9 * x ** 6 - 2.516e-7 * x ** 5 + 1.323e-5 * x ** 4 - 2.676e-4 * x ** 3 + 1.0376e-3 * x ** 2
    else:
        return 0.0072917 * x ** 2 - 0.672917 * x + 15.5

def arthur_n(x):
    if 0 <= x <= 6:
        return 1.0
    elif 6 <= x <= 9:
        return (-x / 30.0) + (6.0 / 5.0)
    elif 9 <= x <= 12:
        return (-x / 20.0) + (27.0 / 20.0)
    else:
        return 0.75

def arthur_kms(board):
	return arthur_n(sum(board)) * arthur_m(max(board))
