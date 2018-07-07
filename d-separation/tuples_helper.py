def is_node_in_blocked(tuples, node):
    for x, y, z in tuples:
        if (x==node or y==node) and z:
            return True 
    return False

def get_blocked_with_node_n(tuples, node):
    result=[]
    for x, y, z in tuples:
        if x==node and z:
            result+=[y]
    return result