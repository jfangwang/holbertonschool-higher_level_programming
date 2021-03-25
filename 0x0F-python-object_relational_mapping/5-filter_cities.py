#!/usr/bin/python3
""" Filter states """
if __name__ == "__main__":
    import MySQLdb
    import sys
    argv = sys.argv
    state_id = 0
    if len(argv) != 5:
        print("USAGE: ./0-select_states.py username password\
            database_name state_name")
        exit()
    try:
        db = MySQLdb.connect(host="localhost", user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306)
    except:
        print("invalid credentials")
    cur = db.cursor()
    # IDK how to do this in one sql query...rip
    cur.execute("Select states.id from states WHERE states.name = '{}'"
                .format(argv[4]))
    state_id = cur.fetchone()
    if state_id is None:
        state_id = (0,)
    cur.execute("Select cities.name from cities WHERE cities.state_id = {};"
                .format(state_id[0]))
    rows = cur.fetchall()
    if len(rows) > 0:
        for a in range(0, len(rows)):
            if len(rows) - 1 > a:
                print(rows[a][0], end=', ')
        print(rows[a][0])
    cur.close()
    db.close()
