import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
from problem import fitnessFunction, showProducts

fitness = mlrose.CustomFitness(fitnessFunction)
problem = mlrose.DiscreteOpt(length = 14, fitness_fn = fitness, maximize= True, max_val = 2)
bestSoluction, bestCost = mlrose.simulated_annealing(problem, schedule=mlrose.ArithDecay())

print('Soluction: ', bestSoluction)
showProducts(bestSoluction)