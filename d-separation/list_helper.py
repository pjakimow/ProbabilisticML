def get_index(list, el):
  if el in list:
    return list.index(el)
  return -1
    
def contains(list, el):
  return True if get_index(list, el)!=-1 else False

def get_indexes(list, elements):  
  indexes=[]
  
  for el in elements:
    index=get_index(list, el)
    if index != -1:
      indexes+=[index] 
  
  return indexes

def contains_at_least_one(list, elements):  
  for el in elements:
    if get_index(list, el)!=-1:
      return True
  return False