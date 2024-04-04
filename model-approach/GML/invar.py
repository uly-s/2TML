invar = []
data = ['x', 'y', 'z']

x = 1

f = lambda x: x > 0

print(f(x))

invar.append(f)

print(invar)

f = lambda x: x % 2 != 0

invar.append(f)

invar.append(lambda x: x in data)

print(invar)

for f in invar:
  print(f(x))