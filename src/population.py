import lottery

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
            subject.append(lottery.range((0,1)))
    return subject

def __integer_subject(size, bounds):
	subject = []
	for _ in range(size):
		subject.append(lottery.range(bounds))
	return subject

def __permuted_integer_subject(size, bounds):
	subject = []
	for i in range(size):
		subject.append(i)
	lottery.shuffle(subject)
	return subject

def __float_subject(size, bounds):
	subject = []
	realBounds = (bounds[0]*100, bounds[1]*100)
	for _ in range(size):
		subject.append(lottery.range(realBounds)/100)
	return subject

condifications = {
	'BIN' : __binary_subject,
	'INT' : __integer_subject,
	'INT-PERM' : __permuted_integer_subject,
	'FLOAT' : __float_subject
}
