import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
# print(movies)
# for movie in movies:
#     print(movie.values())

with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()
