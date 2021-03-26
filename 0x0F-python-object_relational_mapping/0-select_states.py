#!/usr/bin/python3
""" Get all states"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    argv = sys.argv
    if len(argv) != 4:
        print("USAGE: ./0-select_states.py username password database_name")
        exit()
    try:
        db = MySQLdb.connect(host="localhost", user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306)
    except:
        print()
    cur = db.cursor()
    cur.execute("Select * from states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
