#Graph and weighted graph in Python.

class Graph:
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex):
    self.vertices[vertex] = []

  def add_edge(self, source, target):
    self.vertices[source].append(target)

#weight graph
# class WeightGraph:
#   def __init__(self):
#     self.graph = Graph()
#     def add_vertex(self, vertex):
#       return self.graph.add_vertex(vertex)
#     def add_edge(self, source, target, weight):
#       if not (source in self.graph.vertices and target in self.graph.vertices):
#         raise Exception("Source or Target Vertex does not exist")
#       else:
#         #finish the code below.

class WeightedGraph:
  def __init__(self):
    self.vertices = {}
  
  def add_vertex(self, vertex):
    # Set the data for the vertex
    self.vertices[vertex] = []
    
  def add_edge(self, source, target, weight):
    # Set the weight
    self.vertices[source].append([target, weight])

my_graph = WeightedGraph()

# Create the vertices
my_graph.add_vertex('Paris')
my_graph.add_vertex('Toulouse')
my_graph.add_vertex('Biarritz')

# Create the edges
my_graph.add_edge('Paris', 'Toulouse', 678)
my_graph.add_edge('Toulouse', 'Biarritz', 312)
my_graph.add_edge('Biarritz', 'Paris', 783)