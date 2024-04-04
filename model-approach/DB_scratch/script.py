from __future__ import print_function

import sys
py3=sys.version_info >= (3, 0)
def inext(v):  # next value from iterator
    return next(v) if py3 else v.next()


import apsw
from QOL import *

###
### Check we have the expected version of apsw and sqlite
###

print ("      Using APSW file",apsw.__file__)                # from the extension module
print ("         APSW version",apsw.apswversion())           # from the extension module
print ("   SQLite lib version",apsw.sqlitelibversion())      # from the sqlite library code
print ("SQLite header version",apsw.SQLITE_VERSION_NUMBER)   # from the sqlite header file at compile time




cmd = """create table base_attributes (
            name TEXT PRIMARY KEY,
            desc TEXT,
            refs BLOB);"""

cursor.execute(cmd)

insert('base_attributes', ('bar', 'IQ', str([1, 2, 3, 4])))

select['table']('base_attributes')

def print_table(table):
    cursor.execute("select * from {}".format(table))
    print(cursor.getdescription())
    for cols in cursor.execute("select * from {}".format(table)):
          # shows column names and declared types
        print(cols)

row = cursor.execute("""select refs from base_attributes where name={}""".format('"bar"'))

T = tuple(row)[0]

print(T)

L = list(T[0])

print(L) # LOOK INTO JSON LOADS / JSON MOD FOR THIS