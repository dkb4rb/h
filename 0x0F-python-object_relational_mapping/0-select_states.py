#!/usr/bin/python3

import sys
import MySQLdb

if name == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    prompt = db.cursor()
    prompt.execute("SELECT * FROM states")
    [print[state] for state in prompt.fetchall()]
