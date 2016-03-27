from gamestate import Game_State
from functions import *
from copy import deepcopy
from sys import argv
import jsonpickle

def play_game(player1, player2, startstate, log):
	current_state = deepcopy(startstate)
	game_over = False
	player_1_turn = True
	
	play_history = []
	current_turn = 0
	
	while not game_over:
		if log: log_replay(play_history)
		current_state.print_gameboard()
		print()
		played = False
		while not played:
			if player_1_turn:
				player_selection = player1.get_selection(current_state)
			else:
				player_selection = player2.get_selection(current_state)
			if player_selection == "undo":
				num_turns = -int(input("By how many turns? "))
				play_history = play_history[:num_turns]
				current_state = current_turn + num_turns
				current_turn += num_turns
				current_state = play_history[current_turn]
			slot_to_remove = get_slot(player_selection, player_1_turn)
			if slot_to_remove == -1:
				cls()
				print("This is not a valid turn!")
				current_state.print_gameboard()
			else:
				next_state = play(current_state, slot_to_remove, player_1_turn)
				if next_state.is_state_legal():
					played = True
					play_history.append(deepcopy(current_state))
					current_state = next_state
					player_1_turn = not player_1_turn
					cls()
