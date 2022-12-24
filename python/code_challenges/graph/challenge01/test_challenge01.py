# Write your test here

import pytest 
from challenge01 import Graph 

def test_dfs():
  graph = Graph()

  a = graph.add_node("A")
  b = graph.add_node("B")
  c = graph.add_node("C")
  d = graph.add_node("D")

  graph.add_edge(a,b)
  graph.add_edge(a,c)
  graph.add_edge(c,b)
  graph.add_edge(d,b)
  graph.add_edge(d,c)

  assert graph.breadth_first(a)==['A', 'B', 'C', 'D']
     
