import json
from pathlib import Path

path = Path("movies.json")
data = path.read_text()
print("data: ", data)
print(type(data))
movies = json.loads(data)
print(movies[0])
print(type(movies))
