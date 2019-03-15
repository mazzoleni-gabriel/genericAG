import initPopulation as pop

#PARAMETERS
BOUNDS = (-5, 10)
COD = 'REAL'
POPULATION_SIZE = 10
CROMOSSOME_SIZE = 5

print(pop.init_population(POPULATION_SIZE, CROMOSSOME_SIZE, 'BIN', BOUNDS))
print(pop.init_population(POPULATION_SIZE, CROMOSSOME_SIZE, 'INT', BOUNDS))
print(pop.init_population(POPULATION_SIZE, CROMOSSOME_SIZE, 'INT-PERM', BOUNDS))
print(pop.init_population(POPULATION_SIZE, CROMOSSOME_SIZE, 'REAL', BOUNDS))

