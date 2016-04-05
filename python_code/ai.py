from ai_functions import *

class AI:
	
	def __init__(self, coefficients):
		self.coefficients = coefficients
	
	def get_selection(self, game_state):
		return str(do_turn(self, game_state, self.eval_functions))
	
	def eval_is_largest_stack_increased(self, old_state, new_state, kms):
		coeff = self.coefficients
		
		previous_largest_stack = max(old_state.stones[:6])
		new_largest_stack = max(new_state.stones[:6])

		if new_largest_stack > previous_largest_stack:
			retval = (coeff[0] / arthur_g(kms)) * coeff[1]
		else:
			retval = 0.0

		return retval

	def eval_amount_stones_lost(self, old_state, new_state, kms):
		coeff = self.coefficients
	 
		my_stones_before = sum(old_state.stones[:6])
		my_stones_after = sum(new_state.stones[:6])

		retval = (my_stones_after - my_stones_before) * (coeff[2] * arthur_h(kms))

		return retval

	def eval_amount_bad_stacks_created(self, old_state, new_state, kms):
		coeff = self.coefficients
		
		old_opportunities = 0
		new_opportunities = 0

		for slot in old_state.stones[:6]:
			if 0 < slot < 3:
				old_opportunities += 1

		for slot in new_state.stones[:6]:
			if 0 < slot < 3:
				new_opportunities += 1

		retval = (new_opportunities - old_opportunities) * (coeff[3] * arthur_h(kms))

		return retval


	def eval_amount_bad_opportunities_created(self, old_state, new_state, kms):
		coeff = self.coefficients
		
		old_opportunities = 0
		new_opportunities = 0

		for slot in range(0,6):
			if check_if_slot_capturable_by_enemy(old_state.stones, slot):
				old_opportunities += 1

		for slot in range(0,6):
			if check_if_slot_capturable_by_enemy(new_state.stones, slot):
				new_opportunities += 1

		retval = (new_opportunities - old_opportunities) * (coeff[4] * arthur_h(kms)) + coeff[5] * kms

		return retval

	def eval_is_enemy_forced_to_play_their_last_possible_move_and_thus_lose_the_game_in_a_sad_and_pathetic_way(self, old_state, new_state, kms):
		enemy_slots = new_state.stones[6:]
		enemy_filled_slots = len([val for val in enemy_slots if val != 0])

		retval = 0.0

		if (enemy_filled_slots == 1 and enemy_slots[5] != 0) or new_state.player_1_score >= 24:
			retval = float("inf")

		return retval
	   

	def eval_did_i_open_my_biggest_slot(self, old_state, new_state, kms): #that's what she said huehuehue
		coeff = self.coefficients
		
		my_old_slots = old_state.stones[:6]
		my_new_slots = new_state.stones[:6]

		retval = 0.0

		if max(my_new_slots) < max(my_old_slots):
			retval = coeff[6] * arthur_j(kms) * arthur_k(my_new_slots)

		return retval

	def eval_is_enemy_forced_to_open_their_largest_stack(self, old_state, new_state, kms):
		coeff = self.coefficients
		
		enemy_slots = new_state.stones[6:]
		enemy_filled_slots = len([val for val in enemy_slots if val != 0])
		
		retval = 0.0

		if enemy_filled_slots == 1:
			retval = coeff[7] * arthur_j(kms) * arthur_k(enemy_slots)

		return retval

	def eval_stones_captured(self, old_state, new_state, kms):
		coeff = self.coefficients
		
		score_difference = new_state.player_1_score - old_state.player_1_score
		
		retval = coeff[8] * score_difference * arthur_h(kms)

		return retval


	eval_functions = [eval_is_largest_stack_increased, eval_amount_stones_lost, eval_amount_bad_stacks_created, eval_amount_bad_opportunities_created, eval_is_enemy_forced_to_play_their_last_possible_move_and_thus_lose_the_game_in_a_sad_and_pathetic_way, eval_did_i_open_my_biggest_slot, eval_is_enemy_forced_to_open_their_largest_stack, eval_stones_captured] # holy shit
