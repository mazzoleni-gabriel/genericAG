import population
import fitness as fit
import crossover

POPULATION_SIZE = 10
CROMOSSOME_SIZE = 10
CODIFICATION = 'BIN'
BOUNDS = None

def fitness(bit_list):
	values = break_bit_list(bit_list)
	NS = ajust_scale((0,24), __bitlist_to_int(values[0]), CROMOSSOME_SIZE/2)
	NL = ajust_scale((0,16), __bitlist_to_int(values[1]), CROMOSSOME_SIZE/2)
	L = NS*30 + NL*40
	H = (NS + 2*NL - 40)/(16)
	if H > 0:
		print(str(H) + ":" + str(NS) + ":" + str(NL))
		return L - H
	return L



def ajust_scale(expected_bounds, value, bits):
	return int (0 + ( (expected_bounds[1] - expected_bounds[0])/(2**bits - 1) )*value)

def break_bit_list(bit_list):
	length = int(len(bit_list)/2)
	NS = []
	NL = []
	for i in range(length):
		NS.append(bit_list[i])
		NL.append(bit_list[i+length])
	result = (NS,NL)
	return result

def __bitlist_to_int(bitlist):
	return int("".join(str(i) for i in bitlist), 2)

pop = population.init(POPULATION_SIZE, CROMOSSOME_SIZE, 'BIN', BOUNDS)
# print(pop)
# print(fitness(pop[0]))
print(fit.evaluate(fitness, pop))
