#!/usr/bin/python3

"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv as arg


def main():
    conn = MySQLdb.connect(
        host='localhost', port=3306, user=arg[1], passwd=arg[2], db=arg[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")

    for res in cur.fetchall():
        print(res)


if __name__ == '__main__':
    main()
