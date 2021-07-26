# -*- coding: utf-8 -*-
import mlrose

peoples = [('Lisboa', 'LIS'),
          ('Madrid', 'MAD'),
          ('Paris', 'CDG'),
          ('Dublin', 'DUB'),
          ('Bruxelas', 'BRU'),
          ('Londres', 'LHR')]

destine = 'FCO'

flights = {}

for row in open('flights.txt'):
  origin, destine, departure, arrival, price = row.split(',')
  
  #adiciona dentro do dicionario, caso nao exista esse, e os seguintes ele so adiciona dentro dele, pra nao criar um pra cada
  flights.setdefault((origin, destine), [])
  flights[(origin, destine)].append((departure, arrival, int(price)))
  
# a representação da resposta vai ser em um array de 12 posições(porque sao seis pessoas), cada 2 posições, vai representar uma cidade, os dois primeiros 
# numeros por exemplo, representam o voo de Lisboa, sendo o numero da primira posição o de ida e o da segunda o de volta, pegando 
# o primeiro numero por exemplo, é a posição do voo, se for 0 então é a primeira posição do array fligts correspondente a Lisboa
# schedule = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3]

def showFlights(schedule):
  idFlight = -1
  totalPrice = 0
  
                                     #  Lisboa    LIS   7:39-10:24      219  9:31-11:43     210
  print('%10s %7s %11s %5s %14s %5s' % ('City', 'Abbr', 'Departure', 'Price', 'Arrival', 'Price'))
  
  #imprimir voo para cada uma das pessoas
  #duas barras pra pegar o inteiro
  for i in range(len(schedule) // 2):
    cityName = peoples[i][0]
    origin = peoples[i][1]
    
    idFlight += 1
    
    #pegando o voo de ida
    departure = flights[(origin, destine)][schedule[idFlight]]
    
    totalPrice += departure[2]
    idFlight += 1
    
    arrival = flights[(destine, origin)][schedule[idFlight]]
    
    totalPrice += arrival[2]
    
    print('%10s%8s %5s-%5s %5s %8s-%5s %5s' % (cityName, origin, departure[0], departure[1], departure[2], arrival[0], arrival[1], arrival[2]))
  
  print("Total price: ", totalPrice)

#showFlights([1,2, 3,2, 7,3, 6,3, 2,4, 5,3])

#função para calcular o preço dos voos
def fitnessFunction(schedule):
  idFlight = -1
  totalPrice = 0
  
  for i in range(len(schedule) // 2):
    origin = peoples[i][1]
    idFlight += 1
    departure = flights[(origin, destine)][schedule[idFlight]]
    totalPrice += departure[2]
    idFlight += 1
    arrival = flights[(destine, origin)][schedule[idFlight]]
    totalPrice += arrival[2]
    
  return totalPrice

fitness = mlrose.CustomFitness(fitnessFunction())
problem = mlrose.DiscreteOpt(length = 12, fitness_fn = fitness, maximize = False, max_val = 10)
print(fitnessFunction(fitness))