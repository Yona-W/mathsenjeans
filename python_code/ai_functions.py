import functions
from copy import deepcopy

def do_turn(game):
	game_state = deepcopy(game)
	#import ipdb;ipdb.set_trace()
	scores_per_move = [0, 0, 0, 0, 0, 0]
	for turn in range(0, 6):
		new_state = functions.play(game_state, turn, True)
		if game.stones[turn] == 0:
			#import ipdb;ipdb.set_trace()
			scores_per_move[turn] = -10000000.0
			#print("skipping impossible turn")
		else:
			for function in eval_functions:
				#print("Calling function",function)
				scores_per_move[turn] += function(game_state, new_state, arthur_kms(new_state.stones))
	#import ipdb;ipdb.set_trace()
	best_score = max(scores_per_move)
	print(best_score)
	i = 0
	for score in scores_per_move:
		i += 1
		if score == best_score:
			print(i)
			return i
	

def eval_is_largest_stack_increased(old_state, new_state, kms):
    previous_largest_stack = max(old_state.stones[:6])
    new_largest_stack = max(new_state.stones[:6])

    if new_largest_stack > previous_largest_stack:
        retval = (1.0 / arthur_g(kms)) * 5
    else:
        retval = 0

    return retval

def eval_amount_stones_lost(old_state, new_state, kms):
    my_stones_before = sum(old_state.stones[:6])
    my_stones_after = sum(new_state.stones[:6])

    retval = (my_stones_after - my_stones_before) * ( -2 * arthur_h(kms))

    return retval

def eval_amount_bad_stacks_created(old_state, new_state, kms):
    old_opportunities = 0
    new_opportunities = 0

    for slot in old_state.stones[:6]:
        if 0 < slot < 3:
            old_opportunities += 1

    for slot in new_state.stones[:6]:
        if 0 < slot < 3:
            new_opportunities += 1

    retval = (new_opportunities - old_opportunities) * (-0.5 * arthur_h(kms))

    return retval


def eval_amount_bad_opportunities_created(old_state, new_state, kms):
    old_opportunities = 0
    new_opportunities = 0

    for slot in range(0,6):
        if check_if_slot_capturable_by_enemy(old_state.stones, slot):
            old_opportunities += 1

    for slot in range(0,6):
        if check_if_slot_capturable_by_enemy(new_state.stones, slot):
            new_opportunities += 1

    retval = (new_opportunities - old_opportunities) * (-1 * arthur_h(kms)) + 0.5 * kms

    return retval

def eval_is_enemy_forced_to_play_their_last_possible_move_and_thus_lose_the_game_in_a_sad_and_pathetic_way(old_state, new_state, kms):
    enemy_slots = new_state.stones[6:]
    enemy_filled_slots = len([val for val in enemy_slots if val != 0])

    if enemy_filled_slots == 1 and enemy_slots[0] != 0:
        return float("inf") #infinity motherfucker
    if new_state.player_1_score >= 24:
        return float("inf") #infinity motherfucker
    return 0.0
   

def eval_did_i_open_my_biggest_slot(old_state, new_state, kms): #that's what she said huehuehue
    #import ipdb;ipdb.set_trace()
    my_old_slots = old_state.stones[:6]
    my_new_slots = new_state.stones[:6]

    if max(my_new_slots) < max(my_old_slots):
        return -50.0 * arthur_j(kms) * arthur_k(my_new_slots)
    return 0.0

def eval_is_enemy_forced_to_open_their_largest_stack(old_state, new_state, kms):
    enemy_slots = new_state.stones[6:]
    enemy_filled_slots = len([val for val in enemy_slots if val != 0])

    if enemy_filled_slots == 1:
        return 50.0 * arthur_j(kms) * arthur_k(enemy_slots)
    return 0.0

def eval_stones_captured(old_state, new_state, kms):
    score_difference = new_state.player_1_score - old_state.player_1_score
    return 2 * score_difference * arthur_h(kms)

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

    return (maximum / average) ** 2

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

eval_functions = [eval_is_largest_stack_increased, eval_amount_stones_lost, eval_amount_bad_stacks_created, eval_amount_bad_opportunities_created, eval_is_enemy_forced_to_play_their_last_possible_move_and_thus_lose_the_game_in_a_sad_and_pathetic_way, eval_did_i_open_my_biggest_slot, eval_is_enemy_forced_to_open_their_largest_stack, eval_stones_captured] # holy shit
