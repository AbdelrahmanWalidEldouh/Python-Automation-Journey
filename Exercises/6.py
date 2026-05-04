import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

countries = soup.find_all("div", class_="col-md-4 country")

for country in countries:

    # اسم الدولة
    name = country.find("h3", class_="country-name").text.strip()

    # العاصمة
    capital = country.find("span", class_="country-capital").text.strip()

    # السكان
    population = country.find("span", class_="country-population").text.strip()

    # المساحة (زيادة مفيدة)
    area = country.find("span", class_="country-area").text.strip()

    print(name)
    print("Capital:", capital)
    print("Population:", population)
    print("Area:", area)
    print("-----------")
