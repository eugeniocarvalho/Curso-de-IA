import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
from airportProblem import fitnessFunction, showFlights

#customFitness é pra problema personalizado
fitness = mlrose.CustomFitness(fitnessFunction)
#represetando o problema, DiscreteOpt porque estamos trabalhando com números int(10 voos por cidade), length é o tamanho da solução(12 voos)
#maximize false porque queremos o menores valores das passagens, max_val é no máximo ate 10(0 a 9)
problem = mlrose.DiscreteOpt(length = 12, fitness_fn = fitness, maximize = False, max_val = 10)
# retorna a melhor solução e o melhor custo, unico parametro obrigatório é a representação do problema
bestSoluction, bestCost = mlrose.hill_climb(problem)

print(bestSoluction, bestCost)
showFlights(bestSoluction)