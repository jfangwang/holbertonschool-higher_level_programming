#!/usr/bin/python3
""" Filter states """
if __name__ == "__main__":
    import MySQLdb
    import sys
    argv = sys.argv
    if len(argv) != 4:
        print("USAGE: ./0-select_states.py username password database_name")
        exit()
    try:
        db = MySQLdb.connect(host="localhost", user=argv[1], charset="utf8",
                             passwd=argv[2], db=argv[3], port=3306)
    except:
        print()
    cur = db.cursor()
    cur.execute("SELECT * from states WHERE BINARY name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
