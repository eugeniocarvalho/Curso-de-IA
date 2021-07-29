import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
from airportProblem import fitnessFunction, showFlights

fitness = mlrose.CustomFitness(fitnessFunction)
problem = mlrose.DiscreteOpt(length = 12, fitness_fn = fitness, maximize = False, max_val = 10)

# pop_size é o tamanho da população, mutation_prob é a probabilidade de fazer multações, max_iters é o numero de gerações
bestSolution, bestCost = mlrose.genetic_alg(problem, pop_size = 500, mutation_prob = 0.2)

print(bestSolution)
showFlights(bestSolution)