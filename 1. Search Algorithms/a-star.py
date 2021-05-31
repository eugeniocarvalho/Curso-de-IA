import numpy as np

class OrderedVector():
  def __init__(self, capacity):
    self.capacity = capacity
    self.lastPosition = -1
    self.values = np.empty(self.capacity, dtype=object)
      
  def insertVertex(self, value):
    if self.lastPosition == self.capacity - 1:
      print('Capacity full')
      return

    pos = 0
    for i in range(self.lastPosition + 1):
      pos = i

      if self.values[i].aStarDistance > value.aStarDistance:
        break
      
      if i == self.lastPosition:
        pos = i + 1

    x = self.lastPosition
    while x >= pos:
      self.values[x + 1] = self.values[x]
      x -= 1

    self.values[pos] = value
    self.lastPosition += 1
      
  def show(self):
    if self.lastPosition == -1:
      print('Empty vector')
    else:
      for i in range(self.lastPosition + 1):
        print("{}, {}, {}, {}, {}".format(i, self.values[i].vertex.name, self.values[i].cost, self.values[i].vertex.goal_distance, self.values[i].aStarDistance))
      print()

class Vertex:
  def __init__(self, name, goal_distance):
    self.name = name
    self.visited = False
    self.adjacents = []
    self.goal_distance = goal_distance

  def addAdjacent(self, adjacent):
    self.adjacents.append(adjacent)

  def showAdjacents(self):
    for i in self.adjacents:
      print(i.vertex.name, i.cost)
      
class Adjacent:
  def __init__(self, vertex, cost):
    self.vertex = vertex
    self.cost = cost
    self.aStarDistance = vertex.goal_distance + self.cost
    
class Graph:
  arad = Vertex('Arad', 366)
  zerind = Vertex('Zerind', 374)
  oradea = Vertex('Oradea', 380)
  sibiu = Vertex('Sibiu', 253)
  timisoara = Vertex('Timisoara', 329)
  lugoj = Vertex('Lugoj', 244)
  mehadia = Vertex('Mehadia', 241)
  dobreta = Vertex('Dobreta', 242)
  craiova = Vertex('Craiova', 160)
  rimnicu = Vertex('Rimnicu', 193)
  fagaras = Vertex('Fagaras', 178)
  pitesti = Vertex('Pitesti', 98)
  bucharest = Vertex('Bucharest', 0)
  giurgiu = Vertex('Giurgiu', 77)

  arad.addAdjacent(Adjacent(zerind, 75))
  arad.addAdjacent(Adjacent(sibiu, 140))
  arad.addAdjacent(Adjacent(timisoara, 118))

  zerind.addAdjacent(Adjacent(arad, 75))
  zerind.addAdjacent(Adjacent(oradea, 71))

  oradea.addAdjacent(Adjacent(zerind, 71))
  oradea.addAdjacent(Adjacent(sibiu, 151))

  sibiu.addAdjacent(Adjacent(oradea, 151))
  sibiu.addAdjacent(Adjacent(arad, 140))
  sibiu.addAdjacent(Adjacent(fagaras, 99))
  sibiu.addAdjacent(Adjacent(rimnicu, 80))

  timisoara.addAdjacent(Adjacent(arad, 118))
  timisoara.addAdjacent(Adjacent(lugoj, 111))

  lugoj.addAdjacent(Adjacent(timisoara, 111))
  lugoj.addAdjacent(Adjacent(mehadia, 70))

  mehadia.addAdjacent(Adjacent(lugoj, 70))
  mehadia.addAdjacent(Adjacent(dobreta, 75))

  dobreta.addAdjacent(Adjacent(mehadia, 75))
  dobreta.addAdjacent(Adjacent(craiova, 120))

  craiova.addAdjacent(Adjacent(dobreta, 120))
  craiova.addAdjacent(Adjacent(pitesti, 138))
  craiova.addAdjacent(Adjacent(rimnicu, 146))

  rimnicu.addAdjacent(Adjacent(craiova, 146))
  rimnicu.addAdjacent(Adjacent(sibiu, 80))
  rimnicu.addAdjacent(Adjacent(pitesti, 97))

  fagaras.addAdjacent(Adjacent(sibiu, 99))
  fagaras.addAdjacent(Adjacent(bucharest, 211))

  pitesti.addAdjacent(Adjacent(rimnicu, 97))
  pitesti.addAdjacent(Adjacent(craiova, 138))
  pitesti.addAdjacent(Adjacent(bucharest, 101))

  bucharest.addAdjacent(Adjacent(fagaras, 211))
  bucharest.addAdjacent(Adjacent(pitesti, 101))
  bucharest.addAdjacent(Adjacent(giurgiu, 90))

class AStar():
  def __init__(self, goal):
    self.goal = goal
    self.finded = False
    
  def search(self, current):
    print('------')
    print('Atual {}'.format(current.name))
    current.visited = True
    
    if current == self.goal:
      self.finded = True
    else:
      arr = OrderedVector(len(current.adjacents))
      
      for adj in current.adjacents:
        if adj.vertex.visited == False:
          adj.vertex.visited = True
          arr.insertVertex(adj)
          
      arr.show()
      
      if arr.values[0] != None:
        self.search(arr.values[0].vertex)

graph = Graph()
aSearch = AStar(graph.bucharest)
aSearch.search(graph.arad)