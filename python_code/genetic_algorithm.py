import play_games
from random_player import Random
from ai import AI

import random
import _thread as thread
import time


def test_generation(individuals, threads):

	individual_scores = {}

	for ai in individuals:
		result = test_individual(ai, threads)
		individual_scores[ai] = result
		
	return individual_scores
		
		
def test_individual(individual, threads, games, game_board = [4,4,4,4,4,4,4,4,4,4,4,4]):
	games_per_thread = int(games / threads + 1)
	
	all_games = []
	player_1_win = []
	player_2_win = []
	
	enemy = Random()
	
	for i in range(0, threads):
		thread.start_new_thread(play_games.play, (individual, enemy, game_board, games_per_thread, all_games, player_1_win, player_2_win))
	
	while True:
		if len(all_games) > threads * games_per_thread * 0.9:
			break;
		else:
			print(int(float(len(all_games)) / float(threads * games_per_thread) * 100.0), "%", end="\r") #so ugly
			time.sleep(0.5)

	#while len(all_games) < threads * games_per_thread:
			
	return (len(all_games), len(player_1_win), len(player_2_win))
