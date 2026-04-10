from bs4 import BeautifulSoup
import requests
import re  # regex do wyciągania liczb z ceny

# 1. Strona
url = "http://127.0.0.1:5500/docs/index.html"

# pobieranie strony
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# lista na wszystkie ceny liczbowe
prices = []

# przejscie po kazdym artykule

for car in soup.find_all("article"):
    name_tag = car.find("h2")
    if name_tag:
        name = name_tag.text.strip()
    else:
        name = "Brak nazwy"

    price_tag = car.find(class_="price")
    if price_tag:
        price_text = price_tag.text.strip()
    else:
        price_text = ""

    match = re.search(r"(\d[\d\s]*)", price_text)

    if match:
        number = match.group(1)
        number = number.replace(" ", "")
        number = int(number)

        prices.append(number)
        print(name, "->", number, "PLN")
    else:
        print(name, "->", price_text)


# srednia tylko z liczb
if prices:
    avg_price = sum(prices) / len(prices)
    print(f"\nŚrednia cena liczbowych ogłoszeń: {avg_price:.2f} PLN")
else:
    print("Nie znaleziono żadnej liczbowej ceny.")
