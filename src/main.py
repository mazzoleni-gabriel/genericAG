import random

#PARAMETERS
BOUNDS = (-5, 10)
COD = 'REAL'
POPULATION_SIZE = 10
CROMOSSOME_SIZE = 5


def initSubject(d, codification, bounds):
	if codification == 'BIN':
		return binarySubject(d)
	if codification == 'INT':
		return integerSubject(d, bounds)
	if codification == 'INT-PERM':
		return permutedIntegerSubject(d)
	if codification == 'REAL':
		return realSubject(d, bounds)

def binarySubject(d):
    subject = []
    for _ in range(d):
            subject.append(randomNumber((0,1)))
    return subject

def integerSubject(d, bounds):
	subject = []
	for _ in range(d):
		subject.append(randomNumber(bounds))
	return subject

def permutedIntegerSubject(d):
	subject = []
	for i in range(d):
		subject.append(i)
	random.shuffle(subject)
	return subject

def realSubject(d, bounds):
	subject = []
	realBounds = (bounds[0]*100, bounds[1]*100)
	for _ in range(d):
		subject.append(randomNumber(realBounds)/100)
	return subject

def initPopulation(pop, d, codification, bounds):
	population = []
	for _ in range(pop):
		population.append(initSubject(d, codification, bounds))
	return population

def randomNumber(bounds):
	return random.randrange(bounds[0], bounds[1]+1)

print(initPopulation(POPULATION_SIZE, CROMOSSOME_SIZE, COD, BOUNDS))
