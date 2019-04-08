import lottery

def select(d, evaluations):
	n = len(evaluations)
	new_population = []
	for _ in range(n):
		index = lottery.range((0,n-1))
		neighbourhood = []
		new_population.append(evaluations[index][0])

__get_neighboor(d,n,index, evaluations):
	if index + d > n-1 or index + d < 0:
		#TODO ajustar para não tentar pegar um index fora da lista

