import random

def roll(succes_rate):
	return False if range( (0, 100) ) > succes_rate else True

def range(bounds):
	return random.randrange(bounds[0], bounds[1]+1)

def shuffle(vector):
	return random.shuffle(vector)


