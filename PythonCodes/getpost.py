import json
import requests

r1 = requests.post(
    "https://simple-books-api.glitch.me/orders",
    json={"bookId": 1, "customerName": "JsonSeed"},
    headers={
        "Authorization": "22e4a6f46cf71f602ecef7c3e7fc56a273595277e31c572756316433a5b3fa25"
    },
)

r2 = requests.get(
    "https://simple-books-api.glitch.me/orders",
    headers={
        "Authorization": "22e4a6f46cf71f602ecef7c3e7fc56a273595277e31c572756316433a5b3fa25"
    },
)

id = "tyRl3kxIpHwy5Zr79cHfh"
r3 = requests.delete(
    f"https://simple-books-api.glitch.me/orders/{id}",
    # json={ "customerName": "RefatSyder" },
    # json={"bookId": 4, "customerName": "JsonSeed"},
    headers={
        "Authorization": "22e4a6f46cf71f602ecef7c3e7fc56a273595277e31c572756316433a5b3fa25"
    },
)

data = r2.json()

print(data)

with open("newdata.json", "w") as file:
    json.dump(data, file)
print()
