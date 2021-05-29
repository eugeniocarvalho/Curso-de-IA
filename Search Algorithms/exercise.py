import numpy as np

class OrderedVectorAStar():
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
      self.values[x+1] = self.values[x]
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

class OrderedVectorGreedy():
  def __init__(self, capacity):
    self.capacity = capacity
    self.lastPosition = -1
    self.values = np.empty(self.capacity, dtype=object)

  def show(self):
    if self.lastPosition == -1:
      print('Empty Vector')
    else:
      for i in range(self.lastPosition + 1):
        print(i, '', self.values[i].name, '', self.values[i].goal_distance)
      print()
  
  def insertVertex(self, value):
    if self.lastPosition == self.capacity - 1:
      print('Capacity full')
      return

    pos = 0
    for i in range(self.lastPosition + 1):
      pos = i

      if self.values[i].goal_distance > value.goal_distance:
        break
      
      if i == self.lastPosition:
        pos = i + 1

    x = self.lastPosition
    while x >= pos:
      self.values[x + 1] = self.values[x]
      x -= 1

    self.values[pos] = value
    self.lastPosition += 1
    
  def __init__(self, capacity):
    self.capacity = capacity
    self.lastPosition = -1
    self.values = np.empty(self.capacity, dtype=object)

  def show(self):
    if self.lastPosition == -1:
      print('Empty Vector')
    else:
      for i in range(self.lastPosition + 1):
        print(i, '', self.values[i].name, '', self.values[i].goal_distance)
      print()
  
  def insertVertex(self, value):
    if self.lastPosition == self.capacity - 1:
      print('Capacity full')
      return

    pos = 0
    for i in range(self.lastPosition + 1):
      pos = i

      if self.values[i].goal_distance > value.goal_distance:
        break
      
      if i == self.lastPosition:
        pos = i + 1

    x = self.lastPosition
    while x >= pos:
      self.values[x + 1] = self.values[x]
      x -= 1

    self.values[pos] = value
    self.lastPosition += 1
    
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
    self.aStarDistance = self.vertex.goal_distance + cost
  
class Graph:
  portoUniao = Vertex('Porto União', 203)
  pauloFrontin = Vertex('Paulo Frontin', 172)
  canoinhas = Vertex('Canoinhas', 141)
  tresBarras = Vertex('Três Barras', 131)
  saoMateusDoSul = Vertex('São Mateus do Sul', 123)
  irati = Vertex('Irati', 139)
  curitiba = Vertex('Curitiba', 0)
  palmeira = Vertex('Palmeira', 59)
  mafra = Vertex('Mafra', 94)
  campoLargo = Vertex('Campo Largo', 27)
  balsaNova = Vertex('Balsa Nova', 41)
  lapa = Vertex('Lapa', 74)
  tijucas = Vertex('Tijucas do Sul', 56)
  araucaria = Vertex('Araucária', 23)
  saoJoseDosPinhais = Vertex('São José dos Pinhais', 13)
  contenda = Vertex('Contenda', 39)
  
  portoUniao.addAdjacent(Adjacent(pauloFrontin, 46))
  portoUniao.addAdjacent(Adjacent(saoMateusDoSul, 87))
  portoUniao.addAdjacent(Adjacent(canoinhas, 78))
  
  pauloFrontin.addAdjacent(Adjacent(irati, 75))
  pauloFrontin.addAdjacent(Adjacent(portoUniao, 46))
  
  canoinhas.addAdjacent(Adjacent(portoUniao, 78))
  canoinhas.addAdjacent(Adjacent(tresBarras, 12))
  canoinhas.addAdjacent(Adjacent(mafra, 66))
  
  irati.addAdjacent(Adjacent(pauloFrontin, 75))
  irati.addAdjacent(Adjacent(saoMateusDoSul, 57))
  irati.addAdjacent(Adjacent(palmeira, 75))
  
  saoMateusDoSul.addAdjacent(Adjacent(portoUniao, 87))
  saoMateusDoSul.addAdjacent(Adjacent(tresBarras, 43))
  saoMateusDoSul.addAdjacent(Adjacent(lapa, 60))
  saoMateusDoSul.addAdjacent(Adjacent(palmeira, 77))
  saoMateusDoSul.addAdjacent(Adjacent(irati, 57))
  
  tresBarras.addAdjacent(Adjacent(saoMateusDoSul, 43))
  tresBarras.addAdjacent(Adjacent(canoinhas, 12))
  
  palmeira.addAdjacent(Adjacent(irati, 75))
  palmeira.addAdjacent(Adjacent(saoMateusDoSul, 77))
  palmeira.addAdjacent(Adjacent(campoLargo, 55))
  
  contenda.addAdjacent(Adjacent(balsaNova, 19))
  contenda.addAdjacent(Adjacent(araucaria, 18))
  contenda.addAdjacent(Adjacent(lapa, 26))
  
  lapa.addAdjacent(Adjacent(contenda, 26))
  lapa.addAdjacent(Adjacent(saoMateusDoSul, 60))
  lapa.addAdjacent(Adjacent(mafra, 57))
  
  mafra.addAdjacent(Adjacent(canoinhas, 66))
  mafra.addAdjacent(Adjacent(lapa, 57))
  mafra.addAdjacent(Adjacent(tijucas, 99))
  
  campoLargo.addAdjacent(Adjacent(palmeira, 55))
  campoLargo.addAdjacent(Adjacent(balsaNova, 22))
  campoLargo.addAdjacent(Adjacent(curitiba, 29))
  
  balsaNova.addAdjacent(Adjacent(campoLargo, 22))
  balsaNova.addAdjacent(Adjacent(contenda, 19))
  balsaNova.addAdjacent(Adjacent(curitiba, 59))
  
  araucaria.addAdjacent(Adjacent(contenda, 18))
  araucaria.addAdjacent(Adjacent(curitiba, 37))
  
  tijucas.addAdjacent(Adjacent(mafra, 99))
  tijucas.addAdjacent(Adjacent(saoJoseDosPinhais, 49))
  
  curitiba.addAdjacent(Adjacent(campoLargo, 29))
  curitiba.addAdjacent(Adjacent(balsaNova, 59))
  curitiba.addAdjacent(Adjacent(araucaria, 37))
  curitiba.addAdjacent(Adjacent(saoJoseDosPinhais, 15))
  
  saoJoseDosPinhais.addAdjacent(Adjacent(curitiba, 15))
  saoJoseDosPinhais.addAdjacent(Adjacent(tijucas, 49))
  
class Greedy():
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
      arr = OrderedVectorGreedy(len(current.adjacents))
      
      for adj in current.adjacents:
        if adj.vertex.visited == False:
          adj.vertex.visited == True
          arr.insertVertex(adj.vertex)
          
      arr.show()
      
      if arr.values[0] != None:
        self.search(arr.values[0])
  
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
      arr = OrderedVectorAStar(len(current.adjacents))
      
      for adj in current.adjacents:
        if adj.vertex.visited == False:
          adj.vertex.visited = True
          arr.insertVertex(adj)
        
      arr.show()
      
      if arr.values[0] != None:
        self.search(arr.values[0].vertex)
        
#Busca gulosa
graph = Graph()
greedy = Greedy(graph.curitiba)
greedy.search(graph.portoUniao)

# print('\n\nBusca A*\n')

# graph2 = Graph()
# aSearch = AStar(graph2.curitiba)
# aSearch.search(graph.portoUniao)