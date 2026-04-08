import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://example.com"
response = requests.get(url, verify=False)

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(f"Page title is: {soup.title.text}")

links = soup.find_all("a")

for link in links:
    print(link.get("href"))
