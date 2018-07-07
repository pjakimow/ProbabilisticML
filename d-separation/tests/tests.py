import networkx as nx
import unittest
import d_separation as dsep
import list_helper as h
import tuples_helper as th

class TestDSeparationMethods(unittest.TestCase):
   
    #@unittest.SkipTest    
    def test_h_t_for_path_and_one_c(self):
        G=nx.Graph().to_directed()
        G.add_nodes_from(range(1,9))
        G.add_edges_from([(1,3),(2,3), (3,4),(3,8),(4,6),(5,6),(6,7)])
        
        C=[3]
        
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 1, 4)][0]
        index=h.get_indexes(path, C)[0]  
        self.assertTrue(dsep.is_path_head_tail_blocked_by_c(G, path, index))
        
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 1, 7)][0]
        index=h.get_indexes(path, C)[0]  
        self.assertTrue(dsep.is_path_head_tail_blocked_by_c(G, path, index))
        
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 1, 5)][0]
        index=h.get_indexes(path, C)[0]  
        self.assertTrue(dsep.is_path_head_tail_blocked_by_c(G, path, index))
        
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 2, 7)][0]
        index=h.get_indexes(path, [6])[0]  
        self.assertTrue(dsep.is_path_head_tail_blocked_by_c(G, path, index))
        
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 2, 7)][0]
        self.assertFalse(dsep.is_path_head_tail_blocked_by_c(G, path, -1))
        
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 2, 7)][0]
        self.assertFalse(dsep.is_path_head_tail_blocked_by_c(G, path, 10))

        path=[path for path in nx.all_simple_paths(G.to_undirected(), 1, 2)][0]
        index=h.get_indexes(path, C)[0]  
        self.assertFalse(dsep.is_path_head_tail_blocked_by_c(G, path, index))
    
   # @unittest.SkipTest    
    def test_t_t_blocked_for_path_and_one_c(self):
        G=nx.Graph().to_directed()
        G.add_nodes_from(range(1,9))
        G.add_edges_from([(1,3),(2,3), (3,4),(3,8),(4,6),(5,6),(6,7)])
        
        C=[3]
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 1, 4)][0]
        index=h.get_indexes(path, C)[0]  
        self.assertFalse(dsep.is_path_tail_tail_blocked_by_c(G, path, index))
        
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 1, 2)][0]
        index=h.get_indexes(path, C)[0]  
        self.assertFalse(dsep.is_path_tail_tail_blocked_by_c(G, path, index))
        
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 4, 8)][0]
        index=h.get_indexes(path, C)[0]  
        self.assertTrue(dsep.is_path_tail_tail_blocked_by_c(G, path, index))
        
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 8, 4)][0]
        index=h.get_indexes(path, C)[0]  
        self.assertTrue(dsep.is_path_tail_tail_blocked_by_c(G, path, index))
        
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 3, 8)][0]
        index=h.get_indexes(path, C)[0]  
        self.assertFalse(dsep.is_path_tail_tail_blocked_by_c(G, path, index))
        
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 8, 5)][0]
        index=h.get_indexes(path, C)[0]  
        self.assertTrue(dsep.is_path_tail_tail_blocked_by_c(G, path, index))
   
    #@unittest.SkipTest
    def test_h_h_blocked_for_path(self):
        G=nx.Graph().to_directed()
        G.add_nodes_from(range(1,9))
        G.add_edges_from([(1,3),(2,3), (3,4),(3,8),(4,6),(5,6),(6,7)])
        
        C=[3]
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 1, 2)][0]
        self.assertFalse(dsep.is_path_head_head_blocked(G, path, C))
        
        C=[4]
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 1, 2)][0]
        self.assertFalse(dsep.is_path_head_head_blocked(G, path, C))
        
        C=[3]
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 4, 5)][0]
        self.assertTrue(dsep.is_path_head_head_blocked(G, path, C))
        
        C=[7]
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 4, 5)][0]
        self.assertFalse(dsep.is_path_head_head_blocked(G, path, C))
        
        C=[5,1,2,3,8]
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 4, 5)][0]
        self.assertTrue(dsep.is_path_head_head_blocked(G, path, C))
        
        C=[5,1,2,3,8,7]
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 4, 5)][0]
        self.assertFalse(dsep.is_path_head_head_blocked(G, path, C))
    
    #@unittest.SkipTest    
    def test_is_path_blocked(self):
        G=nx.Graph().to_directed()
        G.add_nodes_from(range(1,9))
        G.add_edges_from([(1,3),(2,3), (3,4),(3,8),(4,6),(5,6),(6,7)])
        
        C=[2, 8, 5]
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 1, 7)][0]
        self.assertFalse(dsep.is_path_blocked(G, path, C))
        
        C=[2, 8, 5, 3]
        self.assertTrue(dsep.is_path_blocked(G, path, C))
        
        C=[3]
        path=[path for path in nx.all_simple_paths(G.to_undirected(), 8, 6)][0]
        self.assertTrue(dsep.is_path_blocked(G, path, C))
        
    #@unittest.SkipTest   
    def test_more_paths_blocked(self):
        G=nx.Graph().to_directed()
        G.add_nodes_from(range(1,9))
        G.add_edges_from([(1,3),(2,3), (3,4),(3,8),(4,6),(5,6),(6,7)])
        G.add_edges_from([(1,5)])
        
        C=[3]
        paths=[path for path in nx.all_simple_paths(G.to_undirected(), 2, 5)]
        self.assertFalse(dsep.is_path_blocked(G, paths[0], C))
        self.assertTrue(dsep.is_path_blocked(G, paths[1], C))
        self.assertFalse(dsep.all_paths_blocked(G, 2, 5, C))
        
        paths=[path for path in nx.all_simple_paths(G.to_undirected(), 2, 7)]
        self.assertFalse(dsep.is_path_blocked(G, paths[0], C))
        self.assertTrue(dsep.is_path_blocked(G, paths[1], C))
        self.assertFalse(dsep.all_paths_blocked(G, 2, 7, C))
        
        paths=[path for path in nx.all_simple_paths(G.to_undirected(), 2, 4)]
        self.assertTrue(dsep.is_path_blocked(G, paths[0], C))
        self.assertTrue(dsep.is_path_blocked(G, paths[1], C))
        self.assertTrue(dsep.all_paths_blocked(G, 2, 4, C))
        
        paths=[path for path in nx.all_simple_paths(G.to_undirected(), 7, 8)]
        self.assertTrue(dsep.is_path_blocked(G, paths[0], C))
        self.assertTrue(dsep.is_path_blocked(G, paths[1], C))
        self.assertTrue(dsep.all_paths_blocked(G, 7, 8, C))
         
    #@unittest.SkipTest
    def test_all_paths_blocked(self):
        G=nx.Graph().to_directed()
        G.add_nodes_from(range(1,9))
        G.add_edges_from([(1,3),(2,3), (3,4),(3,8),(4,6),(5,6),(6,7)])
        
        C=[2, 8, 5]
        self.assertFalse(dsep.all_paths_blocked(G, 1, 7, C))
        
        C=[2, 8, 5, 3]
        self.assertTrue(dsep.all_paths_blocked(G, 1, 7, C))
        
        C=[3]
        self.assertTrue(dsep.all_paths_blocked(G, 8, 6, C))
        
        C=[7]
        self.assertFalse(dsep.all_paths_blocked(G, 8, 6, C))
    
    #@unittest.SkipTest   
    def test_compute_d_separation(self):
        G=nx.Graph().to_directed()
        G.add_nodes_from(range(1,9))
        G.add_edges_from([(1,3),(2,3), (3,4),(3,8),(4,6),(5,6),(6,7)])
        
        C=[3]
        paars=dsep.compute_d_separation(G, C)
        blocked = th.get_blocked_with_node_n(paars, 1)
        self.assertSequenceEqual(blocked, [4,5,6,7,8])
        
        C=[3, 7]
        paars=dsep.compute_d_separation(G, C)
        blocked = th.get_blocked_with_node_n(paars, 1)
        print(blocked)
        self.assertSequenceEqual(blocked, [4,5,6,7,8])
        
        
if __name__ == '__main__':
    unittest.main()