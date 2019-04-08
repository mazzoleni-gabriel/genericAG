import lottery

def select(k, kp, evaluations):
	n = len(evaluations)
	new_population = []
	for _ in range(n):
		selecteds = []
		for _ in range(k):
			selecteds.append( evaluations[lottery.range((0, n-1))] )
		if kp >= lottery.range((0,10000))/10000:
			new_population.append(__get_best(selecteds))
		else:
			new_population.append(__get_worse(selecteds))
	return new_population

def __get_best(selecteds):
	index = 0
	for i in range(len(selecteds)):
		if selecteds[i][1] > selecteds[index][1]:
			index = i
	return selecteds[index][0]

def __get_worse(selecteds):
	index = 0
	for i in range(len(selecteds)):
		if selecteds[i][1] < selecteds[index][1]:
			index = i
	return selecteds[index][0]
