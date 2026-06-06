from bs4 import BeautifulSoup
import re  # regex do wyciągania liczb z ceny
import json

MENU_OPTIONS = (
    "1. Wyświetl auta",
    "2. Dodaj auto",
    "3. Średnia cena",
    "4. Łączna wartość",
    "0. Zapisz i wyjdź"
)


# Strona
url = "http://127.0.0.1:5500/docs/index.html"


def load_cars_from_html():

    cars = []
    with open("docs/index.html", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    for car in soup.find_all("article"):

        name_tag = car.find("h2")
        price_tag = car.find(class_="price")
        mileage_tag = car.find(class_="mileage")

        name = name_tag.text.strip() if name_tag else "Brak nazwy"
        price = price_tag.text.strip() if price_tag else "Brak ceny"
        mileage = mileage_tag.text.strip() if mileage_tag else "Brak przebiegu"

        car_data = {
            "name": name,
            "price": price,
            "mileage": mileage
        }

        cars.append(car_data)
    return cars


def show_cars(cars):
    for car in cars:
        print(f"{car['name']} | {car['price']} | {car['mileage']}")


def main():
    cars = load_cars_from_html()
    show_cars(cars)


main()
