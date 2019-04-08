import lottery
import relative_fitness

## ROULET WITHOUT REPOSITION

#receive a list with tuples (cromossome, fitness_value) and returns de new population, fitness should be between 0 and 1
def select(evaluations):
	relative_evaluations = relative_fitness.get(evaluations)
	n = len(evaluations)
	new_population = []
	for _ in range(int(n/2)):
		index = lottery.range((0,n-1))
		while(not lottery.roll(int(relative_evaluations[index][1]))):
			index = lottery.range((0,n-1))
		new_population.append(relative_evaluations[index][0])

		index_2 = lottery.range((0,n-1))
		while(index_2 != index and not lottery.roll(int(relative_evaluations[index_2][1]))):
			index_2 = lottery.range((0,n-1))
		new_population.append(relative_evaluations[index_2][0])
	return new_population
