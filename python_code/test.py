from default_ai import Default_AI
from genetic_algorithm import test_individual

ai = Default_AI()

threads = int(input("How many threads?"))

result = test_individual(ai, threads)

print("Total games:", result[0])
print("AI wins:", result[1])
print("Random wins:", result[2])
