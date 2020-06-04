import os
import time
import apsw

file = "model"

connection = apsw.Connection(file)
cursor = connection.cursor()


def insert(table, values):
    ins = """insert into {} values(?, ?, ?);""".format(table)
    cursor.execute(ins, values)

def print_table(table):
    cursor.execute("select * from {}".format(table))
    print(cursor.getdescription())
    for cols in cursor.execute("select * from {}".format(table)):
          # shows column names and declared types
        print(cols)



build = {}

#insert = {'base_attributes':insert_into}

select = {'table':print_table}