import list_helper as lh
import networkx as nx

def show_colored_graph(G, blocked_nodes, n):
  color_map = []
   
  for node in G:
      if node==n:
          color_map.append('green')
      elif lh.contains(blocked_nodes, node):  
          color_map.append('red')  
      else:
          color_map.append('yellow') 

  nx.draw(G, node_color = color_map, with_labels = True, node_size=2000)
