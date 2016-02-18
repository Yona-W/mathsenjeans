import functions, gamestate, jsonpickle, sys

f = open(sys.argv[1]).read()

gamestates = jsonpickle.decode(f)
cur_turn = 0

for state in gamestates:
	cur_turn += 1
	print "Turn", cur_turn
	state.print_gameboard()
