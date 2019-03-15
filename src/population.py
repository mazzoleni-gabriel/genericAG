import random

def init(populationSize, chromosomeSize, codification, bounds):
	population = []
	for _ in range(populationSize):
		population.append(__init_subject(chromosomeSize, codification, bounds))
	return population

def __init_subject(chromosomeSize, codification, bounds):
	return condifications[codification](chromosomeSize, bounds)

def __binary_subject(size, bounds):
    subject = []
    for _ in range(size):
            subject.append(__random_number((0,1)))
    return subject

def __integer_subject(size, bounds):
	subject = []
	for _ in range(size):
		subject.append(__random_number(bounds))
	return subject

def __permuted_integer_subject(size, bounds):
	subject = []
	for i in range(size):
		subject.append(i)
	random.shuffle(subject)
	return subject

def __real_subject(size, bounds):
	subject = []
	realBounds = (bounds[0]*100, bounds[1]*100)
	for _ in range(size):
		subject.append(__random_number(realBounds)/100)
	return subject

# ! this function should be in a dedicated file with all random gerenators
def __random_number(bounds):
	return random.randrange(bounds[0], bounds[1]+1)

condifications = {
	'BIN' : __binary_subject,
	'INT' : __integer_subject,
	'INT-PERM' : __permuted_integer_subject,
	'REAL' : __real_subject
}
