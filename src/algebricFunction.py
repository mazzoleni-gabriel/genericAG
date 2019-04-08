import math
import population
import fitness as fit
import crossover
import uniform_rank as selection

POPULATION_SIZE = 10
CROMOSSOME_SIZE = 16
CODIFICATION = 'BIN'
BOUNDS = None

def function(x):
	return math.cos(20*x) - (module(x)/2) + ((x**3)/4)

def module(x):
	return -x if x<0 else x

def fitness(bit_list):
	integer_value = __float_value(bit_list)
	if integer_value > 2 or integer_value < -2:
		return 0
	return function(integer_value) + 4

def min_fitness(bit_list):
	fitness(1/fitness(bit_list))

def __float_value(bit_list):
    return __bitlist_to_int(bit_list)/10000 - 2

def __bitlist_to_int(bitlist):
	return int("".join(str(i) for i in bitlist), 2)

def __int_to_bitlist(n):
	return [int(digit) for digit in bin(n)[2:]]

pop = population.init(POPULATION_SIZE, CROMOSSOME_SIZE, 'BIN', BOUNDS)

# evaluated = fit.evaluate(fitness, pop)
# evaluated.sort(key=lambda tup: tup[1], reverse=True)  # sorts in place
# print(evaluated)
# print(list(map(__float_value, pop)))

print(fit.evaluate(fitness, pop))


for _ in range(5000):
	evaluated = fit.evaluate(fitness, pop)
	pop = selection.select(evaluated)
	pop = crossover.single_point(pop, 50, (0,1))
print(evaluated[0][1] - 4)



