import population

POPULATION_SIZE = 10
CROMOSSOME_SIZE = 8
CODIFICATION = 'INT-PERM'
BOUNDS = None

def fitness(cromossome):
	colisions = 0
	size = len(cromossome)
	for i in range(size):
		for j in range(i, size):
			if cromossome[i] == (cromossome[j] + (j - i)) and i != j:
				colisions = colisions + 1
			if cromossome[i] == (cromossome[j] - (j - i)) and i != j:
				colisions = colisions + 1
	return __division(1,colisions)


def evaluate(population):
	evaluations = []
	for i in range(len(population)):
		value = fitness(population[i])
		evaluations.append(value)
	return evaluations

# ! this should be in a dedicated file, will probablybe used a lot
def __division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0


population = population.init(POPULATION_SIZE, CROMOSSOME_SIZE, 'INT-PERM', BOUNDS)

for i in range(len(population)):
	print(population[i])
	print(fitness(population[i]))


