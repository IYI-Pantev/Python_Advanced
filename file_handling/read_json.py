import json

from pathlib import Path

data = Path("movies.json").read_text()


"""The json.loads() function in Python is used to parse
a JSON formatted string and convert it into a Python object,
typically a dictionary or a list. """
movies = json.loads(data)
print(movies[0]["title"])
