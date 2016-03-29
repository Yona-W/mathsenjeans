import game
from gamestate import Game_State

def play(player_1, player_2, games, all_games, games_won_player1, games_won_player2):
	for i in range(0, games):
		result = game.play_game(player_1, player_2, Game_State(0, 0, [4,4,4,4,4,4,4,4,4,4,4,4], -1), False, False)
		if result[0] == 1:
			games_won_player1.append(result[1])
		else:
			games_won_player2.append(result[1])
			
		all_games.append(result[1])