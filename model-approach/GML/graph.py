from base import _node, _edge



class _graph(dict[str:_node]):
  pass


graph = _graph()

def init():
  _edge.keys = graph.keys()
  _node.keys = graph.keys()
  return graph