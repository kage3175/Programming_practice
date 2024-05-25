import networkx as nx


def build_knowledge_graph(concepts):
  try:
      G = nx.DiGraph()
      for i, concept in enumerate(concepts[:20]):
          G.add_node(concept, label=concept)
          if i > 0:
              G.add_edge(concepts[i-1], concept)
      return G
  except Exception as e:
      print("X")
      
g = build_knowledge_graph([1,2,3])
      
print(g.edges)