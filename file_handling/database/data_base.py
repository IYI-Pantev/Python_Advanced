# working with a SQLite database

import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("file_handling\movies.json").read_text())

# print(movies)

with sqlite3.connect("db.sqlite3") as conn:
    # Add your database operations here
    command = "Insert into Movies Values(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()
