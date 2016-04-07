from gamestate import Game_State
from functions import *
from copy import deepcopy
from sys import argv
import jsonpickle
from human import Human
from random_player import Random
from default_ai import Default_AI
import game

log = input("Do you want to log the replay? It will overwrite the previous one! [N]/Y ").lower() == "y"
is_different_start_state = input("Do you want to input a different start state? [N]/Y ").lower() == "y"

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

player_1 = Default_AI()
player_2 = Random()

print(game.play_game(player_1, player_2, current_state, log, False))
