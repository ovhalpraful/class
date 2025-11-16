#------------------------------------------------------------
#DSC 510
#Week 10
#Programming Assignment 10.1 - Using OOPS create CashRegister class & add item(s) in it, calculate the total price of items,
#                              and print the cart in a relevant format.
#Author Praful Ovhal
#Date 11-12-2025

#Change#: 1
#Change(s) Made: Added validations and comments
#Date of Change: 11-13-2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 11-13-2025
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

    #Funtion to add items in the cart
    def add_item(self, price):
        self.item_count += 1
        self.total_price += price

    #Function to return total price in the cart
    @property
    def get_total_price(self):
        return self.total_price

    #Function to return total items in the cart
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
                print("\033[34mThank you for using BRUIN Store.\033[0m")
                break
            elif user_input == 'y':
                try:
                    price = float(input("Enter the price: "))
                    if price <= 0:
                        print("\033[31mPrice cannot be zero or less, please try again.\033[0m")
                        continue
                    else:
                        register.add_item(price)
                        print("\033[32mItem added to the cart successfully.\033[0m")
                except ValueError:
                    print("\033[31mPlease use numbers to enter price.\033[0m")
                    logging.error("Invalid input")
            #Displaying cart contents
            elif user_input == 'c':
                print("Your Cart contents")
                print("-" * 100)
                print(f"{'Total # of items in your cart':<50}{'Total price of the cart':<50}")
                print("-" * 100)
                print(f"{register.get_item_count:<50}{locale.currency(register.get_total_price):<50}")
                print("-" * 100)
            else:
                print("\033[31mYou have not entered the suggested input. Please try again.\033[0m")
                continue
        except KeyboardInterrupt:
            print("\n\033[31mYou have stopped the transaction. Exiting...\033[0m")
            logging.error(f"User stopped the program execution.")
            break

if __name__ == '__main__':
    main()