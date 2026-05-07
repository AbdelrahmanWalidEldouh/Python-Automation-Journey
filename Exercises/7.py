import requests
from bs4 import BeautifulSoup
import pandas as pd

books_ = []

for page in range(1, 11):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print("Page:", page)

    for book in books:

        book_name = book.find("h3").find("a")["title"]
        price = float(book.find("p", class_="price_color").text.replace("Â£", ""))

        books_.append({"Name": book_name, "Price": price})

df = pd.DataFrame(books_)

df.to_csv("books.csv", index=False)
