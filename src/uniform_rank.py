import lottery


def select(evaluations):
	n = len(evaluations)
	evaluations.sort(key=lambda tup: tup[1])
	uniform_fitness = __uniform_fitness(evaluations, n)
	new_population = []
	while len(new_population) < n:
		index = lottery.range((0,n-1))
		if lottery.roll(uniform_fitness[index][1]):
			new_population.append(uniform_fitness[index][0])
	return new_population

def __uniform_fitness(evaluations, n):
	sum = ((1 + n)*(n))/2
	uniform_fitness = []
	for i in range(n):
		uniform_fitness.append( (evaluations[i][0], 100*(i+1)/sum) )
	return uniform_fitness

