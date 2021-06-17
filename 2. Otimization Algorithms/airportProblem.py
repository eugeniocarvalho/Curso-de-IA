people = [('Lisboa', 'LIS'),
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
  
