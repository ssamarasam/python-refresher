import json
from pathlib import Path

movies = [
    {"id": 1, "movie": "Terminator", "year": 1999},
    {"id": 2, "movie": "Cast Away", "year": 1989}
]

data = json.dumps(movies)
print(data)
Path("movies.json").write_text(data)
