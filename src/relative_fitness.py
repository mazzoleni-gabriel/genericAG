def get(evaluations):
	sum = __get_fitness_sum(evaluations)
	relative_fitness = []
	for i in range (len(evaluations)):
		relative = 100 * (evaluations[i][1])/(sum)
		relative_fitness.append( (evaluations[i][0], relative) )
	return relative_fitness

def __get_fitness_sum(evaluations):
	sum = 0
	for i in range(len(evaluations)):
		sum = sum + evaluations[i][1]
	return sum
