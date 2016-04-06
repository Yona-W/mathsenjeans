class Human:
	def __init__(self, is_player_1):
		self.is_player_1 = is_player_1
		
	def get_selection(self, game_state):
		if self.is_player_1:
			return input("It's Player 1's turn! Pick a slot: ").lower()
		else:
			return input("It's Player 2's turn! Pick a slot: ").lower()