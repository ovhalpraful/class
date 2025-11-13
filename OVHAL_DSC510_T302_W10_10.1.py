#------------------------------------------------------------
#DSC 510
#Week 10
#Programming Assignment 10.1 -
#Author Praful Ovhal
#Date 11--2025

#Change#: 1
#Change(s) Made:
#Date of Change: 11--2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 11--2025
#--------------------------------------------------------------
import logging
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Error logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='error.log',  # Logs will be written to this file
    filemode='a'           # Append mode
)

class CashRegister():
    """Cash Register Class is used to register items, calculate total price, & item count."""

    def __init__(self):
        self.item_count = 0
        self.total_price = 0.0

    def add_item(self, price):
        self.item_count += 1
        self.total_price += price

    @property
    def get_total_price(self):
        return self.total_price

    @property
    def get_item_count(self):
        return self.item_count

def main():
    sentinel = 'q'
    register = CashRegister()
    print("Welcome to the BRUIN Store")

    while True:
        try:
            user_input = input(f"Please select a step from the following to perform: \nY: To add item \nC: Go to cart \nQ: To quit \nYou choice: ").strip().lower()
            if user_input == 'q':
                print("Thank you for using BRUIN Store.")
                break
            elif user_input == 'y':
                price = float(input("Enter the price: "))
                if price <= 0:
                    print("Price is less than 0, please try again.")
                    continue
                else:
                    register.add_item(price)
            elif user_input == 'c':
                print("Your Cart contents")
                print("-" * 100)
                print(f"{'Total # of items in your cart':<50}{'Total price of the cart':<50}")
                print("-" * 100)
                print(f"{register.get_item_count:<50}{locale.currency(register.get_total_price):<50}")
                print("-" * 100)
            else:
                print("You have not entered the suggested input. Please select again.")
                continue
        except KeyboardInterrupt:
            print("\nYou have stopped the transaction. Exiting...")
            logging.error(f"User stopped the program execution.")
            break

if __name__ == '__main__':
    main()