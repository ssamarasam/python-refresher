import sqlite3
import json
from pathlib import Path

with sqlite3.connect("db.sqlite3") as conn:
    command = 'SELECT * FROM Movies'
    cursor = conn.execute(command)
    # print(cursor)
    # for movie in cursor:
    #     print(movie[1])

    movies = cursor.fetchall()
    print(movies)
