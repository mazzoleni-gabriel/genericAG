import lottery

# population sort by fitness
def single_point(population, prob):
	new_population = []
	for j in range(int(len(population)/2)):
		childrens = __single_point(population[j*2], population[j*2+1], prob)
		new_population.append(childrens[0])
		new_population.append(childrens[1])
	return new_population

def __single_point(parent_1, parent_2, prob):
	if not lottery.roll(prob):
		return (parent_1, parent_2)
	point = lottery.range( ( 0, len(parent_1) ) )
	children_1 = []
	children_2 = []
	for i in range(point):
		children_1.append(parent_1[i])
		children_2.append(parent_2[i])
	for i in range(point, len(parent_1)):
		children_1.append(parent_2[i])
		children_2.append(parent_1[i])
	return (children_1, children_2)




