from gamestate import Game_State
from functions import *
from copy import deepcopy
from sys import argv
import jsonpickle
import random
import time

def play_game(player1, player2, startstate, log, print_screen = True):
	current_state = deepcopy(startstate)
	game_over = False
	player_1_turn = startstate.is_player_1_turn
	
	play_history = []
	current_turn = 0
	
	inner_loop = 0

	while not game_over:

		inner_loop = inner_loop + 1
		if inner_loop > 200:
#			print("Game was stuck; I cancelled it")
			return (random.randint(1,2), current_state)
		if log: log_replay(play_history)
		if print_screen:
			current_state.print_gameboard()
			time.sleep(1)
			print()
		played = False

		current_loop = 0

		while not played:

			current_loop = current_loop + 1
			if current_loop > 100:
				#print("Game was stuck; I cancelled it")
				return (random.randint(1,2), current_state)

			#import ipdb;ipdb.set_trace()
			if player_1_turn:
				player_selection = player1.get_selection(deepcopy(current_state))
			else:
				player_selection = player2.get_selection(deepcopy(current_state))
			if player_selection == "undo":
				num_turns = -int(input("By how many turns? "))
				play_history = play_history[:num_turns]
				current_state = current_turn + num_turns
				current_turn += num_turns
				current_state = play_history[current_turn]
			slot_to_remove = get_slot(player_selection, player_1_turn)
			if slot_to_remove == -1:
#				cls()
#				print("This is not a valid turn!")
				if print_screen: current_state.print_gameboard()
			else:
				next_state = play(deepcopy(current_state), slot_to_remove, player_1_turn)
				if next_state == None:
#					if player_1_turn: print("error illegal state")
					#return None
					continue

				legal_state = deepcopy(next_state).is_state_legal(player_1_turn)

				#print (legal_state)

				any_legal_states = False
				for i in range(0, 6):
					simulated_state = play(deepcopy(current_state), i, player_1_turn)
					if simulated_state and simulated_state.is_state_legal(True):
						any_legal_states = True
#				print(any_legal_states)
				if not any_legal_states or next_state.is_state_legal(player_1_turn):

					if next_state.get_winning() > 0:
						return (next_state.get_winning(), current_state)
	
					played = True
					play_history.append(deepcopy(current_state))
					current_state = next_state
					player_1_turn = not player_1_turn
					if print_screen: cls()
				else:
					if player_1_turn:
						pass
#						print("Error: illegal state")
#						print(jsonpickle.encode(current_state))
