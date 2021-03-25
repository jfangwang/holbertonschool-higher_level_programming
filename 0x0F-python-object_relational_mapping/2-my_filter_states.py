#!/usr/bin/python3
""" Filter states """
import MySQLdb
import sys
argv = sys.argv
if len(argv) != 5:
    print("USAGE: ./0-select_states.py username password\
           database_name state_name")
    exit()
try:
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
except:
    print("invalid credentials")
cur = db.cursor()
cur.execute("SELECT * from states WHERE BINARY name LIKE '{}';"
            .format(argv[4]))
rows = cur.fetchall()
for row in rows:
    print(row)
