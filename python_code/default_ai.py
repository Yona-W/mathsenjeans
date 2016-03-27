from ai import AI

class Default_AI:
	def __init__(self):
		self.ai = AI([1.0, 5.0, -2.0, -0.5, -1.0, 0.5, -50.0, 50.0, 2.0])
		
	def get_selection(self, game_state):
		return self.ai.get_selection(game_state)