import networkx as nx
import list_helper as lh

def is_path_head_tail_blocked_by_c(G, path, c_index):
    if c_index > 0 and c_index < len(path)-1:#not first and not last element
        return nx.has_path(G, path[c_index-1], path[c_index]) and nx.has_path(G, path[c_index], path[c_index+1])
    return False

def is_path_tail_tail_blocked_by_c(G, path, c_index):
    if c_index > 0 and c_index < len(path)-1:#not first and not last element
        return nx.has_path(G, path[c_index], path[c_index-1]) and nx.has_path(G, path[c_index], path[c_index+1])
    return False
        
def is_path_head_tail_blocked_by_C(G, path, C):
    c_indexes=lh.get_indexes(path, C)
    
    for c_index in c_indexes:
       if is_path_head_tail_blocked_by_c(G, path, c_index):
           return True
    return False

def is_path_tail_tail_blocked_by_C(G, path, C):
    c_indexes=lh.get_indexes(path, C)
    
    for c_index in c_indexes:
       if is_path_tail_tail_blocked_by_c(G, path, c_index):
           return True
    return False 

def is_path_head_head_blocked(G, path, C):
    if len(path) < 3:
        return False
    for v in range(1, len(path)-1): #not first and not last element
        if nx.has_path(G, path[v-1], path[v]) and nx.has_path(G, path[v+1], path[v]):
            if lh.contains(C, path[v]) or lh.contains_at_least_one(C, get_descendants(G, path[v])):
                continue
            else:
                return True
    return False
  
def is_path_blocked(G, path, C):   
    return is_path_head_head_blocked(G, path, C) or is_path_tail_tail_blocked_by_C(G, path, C) or is_path_head_tail_blocked_by_C(G, path, C)

def all_paths_blocked(G, source, target, C):
    if source != target:
        paths=[path for path in nx.all_simple_paths(G.to_undirected(), source, target)]
        
        for path in paths:
            if not is_path_blocked(G, path, C):
                return False
        if len(paths)>0:
            return True
    return False

def compute_d_separation(G, C):
    result=[]
    
    for n in G.nodes():
        for m in G.nodes():
            if m!=n:     
                result += [(n, m, all_paths_blocked(G, n, m, C))]
    
    return result

def get_descendants(G, node):
    return nx.descendants(G, node)

def has_path(G, source, target):
    try:
        length, _ = nx.bidirectional_dijkstra(G, source, target)
        return True if length > 0 else False
    except nx.NetworkXNoPath:
        return False

    
