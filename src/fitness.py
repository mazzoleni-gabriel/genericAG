
def calculate(function, cromossome):
	return function(cromossome)

#return a list of tuples (cromossome, evaluation)
def evaluate(function, population):
	evaluations = []
	for i in range(len(population)):
		value = calculate(function, population[i])
		evaluations.append((population[i], value))
	return evaluations
