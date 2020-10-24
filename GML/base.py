class _edge(object):
  keys = set[str]
  def __init__(self, label: str, src: str = '', dst: str = ''):
    self.label = label
    assert(src in _edge.keys)
    assert(dst in _edge.keys)
    self.src = src
    self.dst = dst


class _node(object):
  keys = set[str]
  def __init__(self, label: str, edges: dict[str:_edge] = {}):
    self.label = label
    self.edges = edges

  def __getitem__(self, label: str):
    return self.edges[label]

  def __setitem__(self, label: str, edge:_edge):
    self.edges[label] = edge




