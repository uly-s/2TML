from classes import Rel, Ent

class _graph(dict[str:Ent]):
  pass


graph = _graph()

def init():
  Rel.keys = graph.keys()
  Ent.keys = graph.keys()
  return graph