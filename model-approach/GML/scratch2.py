from classes import Rel, Ent
from graph import init

G = init()

G['A'] = Ent('A')
G['B'] = Ent('B')

G['A']['knows'] = Rel('knows', 'A', 'B')

G['A'].edges['knows'].invar = [lambda x: x > 0]