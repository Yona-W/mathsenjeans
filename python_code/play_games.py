import game
from gamestate import Game_State
from multiprocessing import Pool

def play(player_1, player_2, board_state, games, threads, all_games, games_won_player1, games_won_player2):

	arguments = [(player_1, player_2, Game_State(0, 0, board_state, -1), False, False)]
	for i in range(0, games - 1):
		arguments.append(arguments[0])

	p = Pool(threads)
	results = p.starmap(game.play_game, arguments)

	print("Done")

	for result in results:
		if result[0] == 1:
			games_won_player1.append(result[1])
		else:
			games_won_player2.append(result[1])

	all_games = games_won_player1 + games_won_player2

	return (all_games, games_won_player1, games_won_player2)
