from base import _node, _edge
from graph import init

G = init()

G['A'] = _node('A')

print(_node.keys)

G['B'] = _node('B')

print(_node.keys)

G['A']['rel'] = _edge('rel', 'A', 'B')

print(G['A'].edges['rel'].label)