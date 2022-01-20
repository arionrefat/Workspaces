import json
import requests

# api-endpoint
URL = "https://simple-books-api.glitch.me/books"

PARAMS = {"id": 1}

r = requests.get(url=URL, params=PARAMS)

data = r.json()

with open("data.json", "w") as file:
    json.dump(data, file)
print()
