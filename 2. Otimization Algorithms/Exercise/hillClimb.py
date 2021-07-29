import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
from problem import fitnessFunction, showProducts

fitness = mlrose.CustomFitness(fitnessFunction)
problem = mlrose.DiscreteOpt(length = 14, fitness_fn = fitness, maximize= True, max_val = 2)
bestSoluction, bestCost = mlrose.hill_climb(problem)

print('Soluction: ', bestSoluction)
showProducts(bestSoluction)