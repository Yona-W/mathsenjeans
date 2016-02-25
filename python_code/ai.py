from gamestate import Game_State
from functions import *
from copy import deepcopy
from sys import argv
import jsonpickle

log = input("Do you want to log the replay? It will overwrite the previous one! [N]/Y ").lower() == "y"
is_different_start_state = input("Do you want to input a different start state? [N]/Y ").lower() == "y"

game_over = False
player_1_turn = True

if is_different_start_state:
	text = "Game_State(0, 0, [" + input("Type it in: ") + "], -1)"
	current_state = eval(text)
else:
	current_state = Game_State(0, 0, [4,4,4,4,4,4,4,4,4,4,4,4], -1)

if len(argv) > 1:
	replay = open(argv[1], "r").read()
	game_states = jsonpickle.decode(replay)
	turn = int(input("On what turn of the replay do you want to start? ")) - 1

	try:
		current_state = game_states[turn]
		player_1_turn = current_state.is_player_1_turn
	except e:
		print("Error: the replay is only", len(game_states), "turns long!")
		exit()

play_history = []
current_turn = 0

while not game_over:
    if log: log_replay(play_history)
    current_state.print_gameboard()
    print()
    played = False
    while not played:
        if player_1_turn:
           player_selection = input("It's Player 1's turn! Pick a slot: ").lower()
        else:
           player_selection = input("It's Player 2's turn! Pick a slot: ").lower()
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
