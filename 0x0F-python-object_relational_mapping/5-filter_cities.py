#!/usr/bin/python3
""" Filter states """
if __name__ == "__main__":
    import MySQLdb
    import sys
    argv = sys.argv
    state_id = 0
    index = 0
    if len(argv) != 5:
        print("USAGE: ./0-select_states.py username password\
            database_name state_name")
        exit()
    try:
        db = MySQLdb.connect(host="localhost", user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306)
    except:
        print()

    # Check for injections
    while argv[4][index].isalpha() and index < len(argv[4]) - 1:
        index += 1
    if argv[4][index].isalpha():
        index += 1
    argv[4] = argv[4][slice(index)]

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE cities.state_id\
                 IN (SELECT states.id FROM states\
                     WHERE states.name = '{}')\
                 ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()
    if len(rows) > 0:
        for a in range(0, len(rows)):
            if len(rows) - 1 > a:
                print(rows[a][0], end=', ')
        print(rows[a][0])
    cur.close()
    db.close()
