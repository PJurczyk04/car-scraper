from bs4 import BeautifulSoup
import re  # regex do wyciągania liczb z ceny
import json

MENU_OPTIONS = (
    "1. Wyświetl auta",
    "2. Średnia cena",
    "3. Łączna wartość",
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


def calculate_total_value(cars):
    total = 0

    for car in cars:
        price = car["price"]

        if price != "Bezcenny":
            price = price.replace(" PLN", "")
            price = price.replace(" ", "")
            price = int(price)

            total += price
    print(f"Łączna wartośća aut: {total} PLN")


def calculate_average_value(cars):
    total = 0
    count = 0
    for car in cars:
        price = car["price"]
        if price != "Bezcenny":
            price = price.replace(" PLN", "")
            price = price.replace(" ", "")
            price = int(price)
            total += price
            count += 1

    average = total / count

    print(f"Średnia cena to: {average:.2f} PLN")


def save_to_json(cars):
    with open("cars.json", "w", encoding="utf-8") as file:
        json.dump(cars, file, ensure_ascii=False, indent=4)

    print("Dane zapisano do cars.json")


def main():
    cars = load_cars_from_html()

    while True:
        for option in MENU_OPTIONS:
            print(option)

        choice = input("Wybierz opcję: ")

        if choice == "0":
            print("Trwa zapisywanie...")
            save_to_json(cars)
            print("Do zobaczenia.")
            break

        elif choice == "1":
            print("Wybrano opcję 1")
            show_cars(cars)

        elif choice == "2":
            print("Wybrano opcję 2")
            calculate_average_value(cars)

        elif choice == "3":
            print("Wybrano opcję 3")
            calculate_total_value(cars)

        else:
            print("Nieprawidłowa opcja.")


main()
