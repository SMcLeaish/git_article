from dataclasses import dataclass, replace
import os

TAX = 0.10
BREAD_PRICE = 1.99
SOUP_PRICE = 11.99


@dataclass(frozen=True, slots=True)
class Food:
    food_type: str
    food_amount: int
    food_price: float

    @property
    def total(self) -> float:
        return self.food_amount * self.food_price


@dataclass(frozen=True, slots=True)
class Receipt:
    foods: list[Food]
    tip_percentage: float
    tax_percentage: float

    @property
    def subtotal(self) -> float:
        return sum(food.total for food in self.foods)

    @property
    def tip_amount(self) -> float:
        return self.subtotal * self.tip_percentage

    @property
    def tax_amount(self) -> float:
        return self.subtotal * self.tax_percentage

    @property
    def grand_total(self) -> float:
        return self.subtotal + self.tip_amount + self.tax_amount


def selection_printer():
    print("Select the item purchased from the list below")
    print("---------------------------------------------")
    print(f"|1| Bread: {BREAD_PRICE}")
    print(f"|2| Soup: {SOUP_PRICE}")
    print("---------------------------------------------")


def prompt_selection():
    try:
        return int(input("Please select: \n"))
    except ValueError:
        return None


def request_tip():
    print("Would you like to leave a tip? Press 1 for yes, 2 to skip.")
    cont = prompt_selection()
    match cont:
        case 1:
            try:
                pct = float(input("Enter tip percentage (e.g. 15 for 15%): \n"))
                return max(0.0, pct / 100.0)
            except ValueError:
                return 0.0
        case _:
            return 0.0


def itemize(receipt: Receipt):
    print("Itemized receipt:")
    for food in receipt.foods:
        print(
            f"{food.food_type} {food.food_amount} @ ${food.food_price:.2f}: ${food.total:.2f} "
        )


def ascii_art():
    f = open("coca_cola.txt", "r")
    coca_cola = f.read()
    print(coca_cola)
    f.close()


def print_receipt(receipt: Receipt):
    _ = os.system("clear")
    ascii_art()
    itemize(receipt)
    print(f"\n     Subtotal: ${receipt.subtotal:.2f}")
    print(f"    Sales Tax: %{TAX * 100:.0f}")
    print(f"          Tax: ${receipt.tax_amount:.2f} +")
    print(f"          Tip: ${receipt.tip_amount:.2f} +")
    print(f"       Total = ${receipt.grand_total:.2f}")


def run_checkout():
    bread = Food("Bread", 0, BREAD_PRICE)
    soup = Food("Soup", 0, SOUP_PRICE)

    while True:
        selection_printer()
        match prompt_selection():
            case 1:
                bread = replace(bread, food_amount=bread.food_amount + 1)
            case 2:
                soup = replace(soup, food_amount=soup.food_amount + 1)
            case _:
                print("Invalid choice, try again.")
                continue
        print("Select another item? (1 = continue, 2 = checkout)")

        match prompt_selection():
            case 1:
                continue
            case 2:
                break
            case _:
                continue

    tip = request_tip()
    receipt = Receipt(foods=[bread, soup], tip_percentage=tip, tax_percentage=TAX)
    print_receipt(receipt)


run_checkout()
