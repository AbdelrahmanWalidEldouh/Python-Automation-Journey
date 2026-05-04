import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

countries = soup.find_all("div", class_="col-md-4 country")

country_information = []
for country in countries:

    name = country.find("h3", class_="country-name").text.strip()

    capital = country.find("span", class_="country-capital").text.strip()

    population = country.find("span", class_="country-population").text.strip()

    area = country.find("span", class_="country-area").text.strip()

    country_information.append(
        {"Country": name, "Capital": capital, "Population": population, "Area": area}
    )

df = pd.DataFrame(country_information)

df.to_excel("country_information.xlsx", index=False)
