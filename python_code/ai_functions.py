import functions

score_mappings = {''}
eval_functions = {''}

def do_turn(game_state):
	scores_per_move = {}
	for turn in range(1, 6):
		scores = score_mappings
		new_state = functions.play(game_state, str(turn), False)
		for (key, function) in eval_functions:
			scores[key] = function(new_state)
		scores_per_move[turn] = sum(scores)
	best_score = max(scores)
	for (turns, score) in scores:
		if score == best_score:
			return score
	
