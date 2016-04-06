from default_ai import Default_AI
from genetic_algorithm import test_individual as simulate_games
import functions

from multiprocessing import cpu_count
from copy import deepcopy

class Monte_Carlo:

	threads = cpu_count() * 2

	def __init__(self, games):
		self.games = games

		self.ai = Default_AI()


	def get_selection(self, game_state):

		game_state = deepcopy(game_state)
		#import ipdb;ipdb.set_trace()
		percent_per_move = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
		for turn in range(0, 6):
			new_state = functions.play(deepcopy(game_state), turn, True)
			if game_state.stones[turn] == 0:
				#import ipdb;ipdb.set_trace()
				percent_per_move[turn] = -1.0
				print("Skipping empty slot", turn + 1)
			else:
				print("Evaluating probability of winning by playing in slot", turn + 1)
				scores = simulate_games(self.ai, self.threads, self.games, deepcopy(new_state).stones)
				percent_per_move[turn] = scores[1] / scores[0]
				print("Probability of winning is", int(percent_per_move[turn] * 100), "%")
		#import ipdb;ipdb.set_trace()
		best_score = max(percent_per_move)
		i = 0
		for score in percent_per_move:
			i += 1
			if score == best_score:
				#print(i)
				return str(i)