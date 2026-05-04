import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books:

    title = book.h3.a["title"]

    linke = book.h3.a["href"]

    price = book.find("p", class_="price_color").text

    rating = book.find("p", class_="star-rating")["class"][1]

    print(title, "-", price, "-", linke, "-", rating)
