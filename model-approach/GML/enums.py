from enum import Enum

classes = Enum('Classes', ['Rogue', 'Thot', 'Daddy'])

print(classes)

print(list(classes))

rog = classes.Rogue

print(rog)