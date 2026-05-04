import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
response.raise_for_status()
users = response.json()

for user in users:
    name = user["name"]
    email = user["email"]
    city = user["address"]["city"]

    print(f"{name} - {email} - {city}")
