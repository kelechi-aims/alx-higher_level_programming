#!/usr/bin/python3
'''
A script that that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
'''
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        'SELECT  cities.id, cities.name, states.name '
        'FROM cities '
        'JOIN states ON cities.state_id = states.id '
        'WHERE states.name = %s '
        'ORDER BY cities.id ASC', (sys.argv[4],)
    )
    result = cursor.fetchall()
    print(', '.join([res[1] for res in result]))
    cursor.close()
    db.close()
