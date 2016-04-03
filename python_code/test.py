from default_ai import Default_AI
from genetic_algorithm import test_individual

ai = Default_AI()

threads = int(input("How many threads?"))
games = int(input("How many games?"))


result = test_individual(ai, threads, games)

print("Total games:", result[0])
print("AI wins:", result[1])
print("Random wins:", result[2])
