import play_games
from random_player import Random
from ai import AI

import random
import time


def test_generation(individuals, threads):

	individual_scores = {}

	for ai in individuals:
		result = test_individual(ai, threads)
		individual_scores[ai] = result
		
	return individual_scores
		
		
def test_individual(individual, threads, games, game_board = [4,4,4,4,4,4,4,4,4,4,4,4]):

	all_games = []
	player_1_win = []
	player_2_win = []
	
	enemy = Random()
	
	results = play_games.play(individual, enemy, game_board, games, threads, all_games, player_1_win, player_2_win)

	all_games = results[0]
	player_1_win = results[1]
	player_2_win = results[2]
			
	return (len(all_games), len(player_1_win), len(player_2_win))
