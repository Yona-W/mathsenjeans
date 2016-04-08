Our strategies:

	Early game: 
	 
		- Prevent 1's and 2's from appearing (would give the opponent a point advantage early on) 
		- Try to build a "tower" (try to transition into midgame, ability to pressure the enemy. If I hoard the stones, they have less -> more capturable patterns 
		- Keep all stones as long as possible (stops the opponent from building a tower, preventing them from entering midgame and, here again, forcing them to create opportunities) 
	 
	Mid game: 
		 
		- Towers seem to give an advantage (sweeping the whole board): ability to circle the board twice lets you score and try to win by points + starves the opponent of stones 
		- I can transform, for instance, a [1101] into a [2212] that I can entirely capture 
		- Get to endgame by mostly clearing the opponent's board. -> keep a tower as well as medium (~5 - 11) stacks to capture those patterns 
	 
	End game: 
	 
		- Try to stall for time as much as possible 
		- Move all stones individually 
		- Start by opening the stacks at the end of the play area and never give the opponent a stone (they'd gain 5 turns). Once they have no more stones, you win (because they have < 24 stones) 

Our Program:

	Dependencies:
		Python 3.4
		jsonpickle
		colorama

		For the Monte Carlo program, Linux is very highly recommended.

	Usage:
		awale_vs_ai.py - Play against our MinMax AI
		awale_vs_human.py - Play against another human
		awale_vs_mc.py - Play against our Monte Carlo AI (many CPU cores recommended!)
		replay.py - Print a replay JSON file
		test.py - Simulate many games


MATh.en.JEANS 2016 - Jonathan Montineri, Lukas Kavan, Arthur Schichl
