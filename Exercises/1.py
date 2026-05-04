import requests

url = "https://httpbin.org/get"

response = requests.get(url)
response.raise_for_status()

print(response.text[:200])
