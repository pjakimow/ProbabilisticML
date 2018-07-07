import networkx as nx
import time
import tuples_helper as th
import d_separation as dsep
import visualization as v

def run_predefined_graph():
    G=nx.Graph().to_directed()
    G.add_nodes_from(['x1','x2','x3','x4','x5','x6','x7','x8'])
    G.add_edges_from([('x1','x3'),('x2','x3'), ('x3','x4'),('x3','x8'),('x4','x6'),('x5','x6'),('x6','x7')])

    C=['x3']
    paars=dsep.compute_d_separation(G, C)
    blocked = th.get_blocked_with_node_n(paars, 'x1')

    v.show_colored_graph(G, blocked, 'x1')

def run_random_graph():
    G=nx.fast_gnp_random_graph(10, 0.3, directed=True)

    C=[6,5,1,2]
    paars=dsep.compute_d_separation(G, C)
    blocked = th.get_blocked_with_node_n(paars, 7)
    v.show_colored_graph(G, blocked, 7)

# =============================================================================
start=time.time()
run_predefined_graph()
#run_random_graph()
print("Time: {}".format(time.time()-start))