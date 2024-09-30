import json
from pathlib import Path
movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990},
]


"""The json.dumps() function in Python is used to convert
a Python object into a JSON formatted string"""
data = json.dumps(movies)

# print(data)

Path("file_handling\movies.json").write_text(data)
