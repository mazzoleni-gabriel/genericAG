import lottery

def mutate(population, prob):
	for i in range(len(population)):
		population[i] = __bin(population[i], prob)
	return population

def __bin(cromossome, prob):
	for i in range(len(cromossome)):
		if lottery.roll(prob):
			cromossome[i] = __bit_flip(cromossome[i])
	return cromossome

def __bit_flip(bit):
	if bit == 0:
		return 1
	return 0
