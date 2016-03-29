import play_games
from random_player import Random
from ai import AI

import random
import _thread as thread


def test_generation(individuals, threads):

	individual_scores = {}

	for ai in individuals:
		result = test_individual(ai, threads)
		individual_scores[ai] = result
		
	return individual_scores
		
		
def test_individual(individual, threads):
	all_games = []
	player_1_win = []
	player_2_win = []
	enemy = Random()
	for i in range(0, threads):
		thread.start_new_thread(play_games.play, (individual, enemy, 100, all_games, player_1_win, player_2_win))
	
	while len(all_games) < threads * 100:
		print(float(len(all_games)) / float(threads), "%")
			
	return (len(all_games), len(player_1_win), len(player_2_win))