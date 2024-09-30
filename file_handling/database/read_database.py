# working with a SQLite database

import sqlite3
import json
from pathlib import Path


# print(movies)

with sqlite3.connect("db.sqlite3") as conn:
    # Add your database operations here
    command = "SELECT * FROM Movies"
    """the execute() method returns
    a cursor object that can be iterated
    to get the rows of the result set."""
    cursor = conn.execute(command)
    # get each row as tuple
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
