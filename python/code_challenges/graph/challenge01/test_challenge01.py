# Write your test here

import pytest 
from challenge01 import bfs 

def test_dfs():
    visited = []
    graph = {
  'A' : ['B','E','C'],
  'B' : ['D'],
  'C' : ['A','F'],
  'D' : ['B','E'],
  'E' : ['A','D','F','G'],
  'F' : ['C','E','H','I'],
  'G' : ['E','H'],
  'H' : ['F','G','K'],
  'I' : ['F','K'],
  'K' : ['H','I']
}
    assert bfs(visited, graph, 'A') ==' A B E C D F G H I K % '
     
