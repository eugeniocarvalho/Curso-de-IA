import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
from problem import fitnessFunction, showProducts

fitness = mlrose.CustomFitness(fitnessFunction)
problem = mlrose.DiscreteOpt(length = 14, fitness_fn = fitness, maximize= True, max_val = 2)
bestSoluction, bestCost = mlrose.genetic_alg(problem, pop_size = 500, mutation_prob = 0.2)

print('Soluction: ', bestSoluction)
showProducts(bestSoluction)