from base import _node, _edge

class Relation(_edge):
  def __init__(self, label:str, src:str = '', dst:str = ''):
    super().__init__(label, src, dst)
    self.invar = list[lambda x:bool]


class Entity(_node):
  def __init__(self, label:str, edges:dict[str:_edge] = {}):
    self.label = label
    self.edges = edges

  def __getitem__(self, label: str):
    return self.edges[label]

  def __setitem__(self, label:str, edge:_edge):
    self.edges[label] = edge






print("yo")
