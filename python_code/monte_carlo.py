from default_ai import Default_AI
from random_player import Random
from genetic_algorithm import test_individual as simulate_games
import functions
import time

from multiprocessing import cpu_count
from copy import deepcopy

class Monte_Carlo:

	threads = cpu_count()

	def __init__(self, games):
		self.games = games

		self.ai = Default_AI()
		#self.ai = Random()


	def get_selection(self, game_state):

		game_state = deepcopy(game_state)
		#import ipdb;ipdb.set_trace()
		percent_per_move = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
		for turn in range(0, 6):
			new_state = functions.play(deepcopy(game_state), turn, True)
			if game_state.stones[turn] == 0:
				#import ipdb;ipdb.set_trace()
				percent_per_move[turn] = -1.0
				print("Je saute la case", turn + 1, "qui est vide")
			else:
				print("Je calcule la probabilité de gagner si je joue en", turn + 1)
				scores = simulate_games(self.ai, self.threads, self.games, deepcopy(new_state).stones)
				percent_per_move[turn] = scores[1] / scores[0]
				print("J'ai une probabilité de", int(percent_per_move[turn] * 100), "% de gagner")
		#import ipdb;ipdb.set_trace()
		best_score = max(percent_per_move)
		i = 0
		for score in percent_per_move:
			i += 1
			if score == best_score:
				print("Je joue en",i)
				time.sleep(1)
				return str(i)
