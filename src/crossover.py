import lottery

# population sort by fitness
def single_point(population, mutation_prob, bounds):
	pop_len = len(population)
	new_population = __cpy_population(pop_len, population)
	point = lottery.range( ( 0, len(population[0]) ) )

	lenght = int( pop_len/4 ) + 1
	for i in range( lenght ):
		childrens = __single_point(population[i], population[lenght-i], point, mutation_prob, bounds)
		new_population.append(childrens[0])
		new_population.append(childrens[1])
	return new_population

def __cpy_population(pop_len, population):
    new_population = []
    for i in range(int(pop_len/2) - 1):
            new_population.append(population[i])
    return new_population

def __mutate(children, mutation_prob, bounds):
	if lottery.roll( mutation_prob ):
		i = lottery.range((0, len(children))) - 1
		children[i] = lottery.range(bounds)

def __single_point(parent_1, parent_2, point, mutation_prob, bounds):
	children_1 = []
	children_2 = []
	for i in range(point):
		children_1.append(parent_1[i])
		children_2.append(parent_2[i])
	for i in range(point, len(parent_1)):
		children_1.append(parent_2[i])
		children_2.append(parent_1[i])
	__mutate(children_1, mutation_prob, bounds)
	__mutate(children_2, mutation_prob, bounds)
	return (children_1, children_2)




