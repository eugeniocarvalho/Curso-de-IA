class Vertex:
  def __init__(self, name):
    self.name = name
    self.visited = False
    self.adjacents = []

  def addAdjacent(self, adjacent):
    self.adjacents.append(adjacent)

  def showAdjacents(self):
    for i in self.adjacents:
      print(i.vertex.name, i.cost)

class Adjacent:
  def __init__(self, vertex, cost):
    self.vertex = vertex
    self.cost = cost
  
class Graph:
  arad = Vertex('Arad')
  zerind = Vertex('Zerind')
  oradea = Vertex('Oradea')
  sibiu = Vertex('Sibiu')
  timisoara = Vertex('Timisoara')
  lugoj = Vertex('Lugoj')
  mehadia = Vertex('Mehadia')
  dobreta = Vertex('Dobreta')
  craiova = Vertex('Craiova')
  rimnicu = Vertex('Rimnicu')
  fagaras = Vertex('Fagaras')
  pitesti = Vertex('Pitesti')
  bucharest = Vertex('Bucharest')
  giurgiu = Vertex('Giurgiu')

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


graph = Graph()

graph.arad.showAdjacents()