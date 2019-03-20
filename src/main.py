import population
import crossover
import lottery

#PARAMETERS
BOUNDS = (-5, 10)
POPULATION_SIZE = 10
CROMOSSOME_SIZE = 5
MUTATION_PROB = 20

# print(population.init(POPULATION_SIZE, CROMOSSOME_SIZE, 'BIN', BOUNDS))
# print(population.init(POPULATION_SIZE, CROMOSSOME_SIZE, 'INT', BOUNDS))
# print(population.init(POPULATION_SIZE, CROMOSSOME_SIZE, 'INT-PERM', BOUNDS))
# print(population.init(POPULATION_SIZE, CROMOSSOME_SIZE, 'FLOAT', BOUNDS))

# print(crossover.single_point_crossover([1,2,99,4,5], [5,4,3,2,1], 4))

population = population.init(POPULATION_SIZE, CROMOSSOME_SIZE, 'INT', BOUNDS)
print(population)
print( crossover.single_point(population, MUTATION_PROB, BOUNDS) )

