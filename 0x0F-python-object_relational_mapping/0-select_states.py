#!/usr/bin/python3
"""
Import libraries
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    prompt = db.cursor()
    prompt.execute("SELECT * FROM states ORDER BY id ASC")
    [print(state) for state in prompt.fetchall()]
    prompt.close()
    db.close()

