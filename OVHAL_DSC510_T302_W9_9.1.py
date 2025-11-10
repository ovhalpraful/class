#------------------------------------------------------------
#DSC 510
#Week 9
#Programming Assignment 9.1 - Take joke category user input and using API get the jokes and display accordingly.
#Author Praful Ovhal
#Date 11-04-2025

#Change#: 1
#Change(s) Made: Added exceptions code and comments
#Date of Change: 11-08-2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 11-08-2025
#--------------------------------------------------------------
import requests
import json
import logging

# Error logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='error.log',  # Logs will be written to this file
    filemode='a'           # Append mode
)

#Getting categories from the mentioned APIs
def get_categories():
    try:
        api_categories = "https://api.chucknorris.io/jokes/categories"
        if requests.head(api_categories).status_code == 200:
            header = {'cache-control': 'no-cache'}
            response = requests.request("GET", api_categories, headers=header)
            categories = json.loads(response.text)
            return categories
        else:
            print("Something went wrong, please try again later.")
            logging.error("Connection error")
            exit()
    except requests.exceptions.RequestException as re:
        logging.error(re)
        print(f"\nSomething went wrong, please try again later.")
        return None

#Based on the selected category input from the user input, retrieve the joke from the API.
def get_joke(selection):
    try:
        api_jokes = f"https://api.chucknorris.io/jokes/random?category={selection}"
        if requests.head(api_jokes).status_code == 200:
            header = {'cache-control': 'no-cache'}
            response = requests.request("GET", api_jokes, headers=header)
            joke = json.loads(response.text)
            return joke['value']
        else:
            print(f"\nSomething went wrong, please try again later.")
            logging.error("Connection error")
            exit()
    except requests.exceptions.RequestException as re:
        logging.error(re)
        print(f"\nSomething went wrong, please try again later.")
        return None

#Printing the output in grid format
def pretty_print_joke(selection):
    joke = get_joke(get_categories()[selection - 1])
    print("-" * len(joke))
    print(f"{'Category':<15}{'Joke':<15}")
    print("-" * len(joke))
    print(f"{get_categories()[selection - 1].upper():<15}{joke:}")
    print("-" * len(joke))

def main():
    try:
        serial_no = 0
        print("\nWelcome to Chuck Norris Jokes Portal.")
        for category in get_categories():
            serial_no += 1
            print(f"{serial_no}.{category.upper()}")

        sentinel = 0
        while True:
            try:
                #Accepting joke category from user.
                selection = int(input(f"\nPlease select jokes category you wish to use. From 1 to {len(get_categories())} OR Press 0 to quit: "))
                if selection == sentinel:
                    print("Thank you for using Chuck Norris Jokes Portal.")
                    exit(0)
                elif 0 < selection <= len(get_categories()):
                    pretty_print_joke(selection)
                else:
                    print(f"Sorry, the jokes category you entered is out of range. Please try again.")
            except ValueError as ve:
                logging.error(ve)
                print(f"\nPlease enter a number from 1 to {len(get_categories())}.")
    except requests.exceptions.RequestException as re:
        logging.error(re)
        print(f"\nSomething went wrong, please try again later.")
    except IndexError as ie:
        logging.error(ie)
        print(f"\nPlease enter a number from 1 to {len(get_categories())}.")
    except KeyboardInterrupt as kie:
        logging.error(kie)
        print(f"\nProgram stopped. Exiting...")

if __name__ == '__main__':
    main()