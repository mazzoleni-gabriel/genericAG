import random

def initPopulation(populationSize, chromosomeSize, codification, bounds):
	population = []
	for _ in range(populationSize):
		population.append(initSubject(chromosomeSize, codification, bounds))
	return population

def initSubject(chromosomeSize, codification, bounds):
	if codification == 'BIN':
		return binarySubject(chromosomeSize)
	if codification == 'INT':
		return integerSubject(chromosomeSize, bounds)
	if codification == 'INT-PERM':
		return permutedIntegerSubject(chromosomeSize)
	if codification == 'REAL':
		return realSubject(chromosomeSize, bounds)

def binarySubject(size):
    subject = []
    for _ in range(size):
            subject.append(randomNumber((0,1)))
    return subject

def integerSubject(size, bounds):
	subject = []
	for _ in range(size):
		subject.append(randomNumber(bounds))
	return subject

def permutedIntegerSubject(size):
	subject = []
	for i in range(size):
		subject.append(i)
	random.shuffle(subject)
	return subject

def realSubject(size, bounds):
	subject = []
	realBounds = (bounds[0]*100, bounds[1]*100)
	for _ in range(size):
		subject.append(randomNumber(realBounds)/100)
	return subject

def randomNumber(bounds):
	return random.randrange(bounds[0], bounds[1]+1)
