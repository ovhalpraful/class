#------------------------------------------------------------
#DSC 510
#Week 11
#Programming Assignment 11.1 - Weather forecast app: Displaying weather using OpenWeatherMap API
#Author Praful Ovhal
#Date 11--2025

#Change#: 1
#Change(s) Made: Added exceptions code and comments
#Date of Change: 11--2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 11--2025
#--------------------------------------------------------------
import requests
import json
import logging

country_code = 'US'
api_key = "f577dc33e820ff8ed415cd0b7189ca33"

# Error logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='error.log',  # Logs will be written to this file
    filemode='a'           # Append mode
)

def get_coordinates(api_coordinates_url):
    try:
        headers = {'cache-control': 'no-cache'}
        response = requests.get(api_coordinates_url, headers=headers)
        coordinates = json.loads(response.text)
        return coordinates
    except requests.exceptions.RequestException as e:
        logging.error(e)
        print("Something went wrong. Please try again later.")
        return None

def get_weather(coordinates, unit):
    try:
        latitude = coordinates['lat']
        longitude = coordinates['lon']
        api_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units={unit}"
        headers = {'cache-control': 'no-cache'}
        response = requests.get(api_weather_url, headers=headers)
        weather = json.loads(response.text)
        return weather
    except requests.exceptions.RequestException as e:
        logging.error(e)
        print("Something went wrong. Please try again later.")
        return None
    except KeyError as e:
        logging.error(e)
        print("Something went wrong. Please try again later.")
        exit()
    except Exception as e:
        logging.error(e)
        print("Something went wrong. Please try again later.")
        return None

def print_weather(weather):
    try:
        print("-"*40)
        print(f"{'Parameters':<30}{'Values':<60}")
        print("-" * 40)
        print(f"{'City':<30}{weather["name"]:<60}")
        print(f"{'Cloud Coverage':<30}{weather["weather"][0]["main"]:<60}")
        print(f"{'Description':<30}{weather["weather"][0]["description"]:<60}")
        print(f"{'Current Temperature':<30}{weather["main"]["temp"]:<60}")
        print(f"{'Max Temperature':<30}{weather["main"]["temp_max"]:<60}")
        print(f"{'Min Temperature':<30}{weather["main"]["temp_min"]:<60}")
        print(f"{'Feels Like':<30}{weather["main"]["feels_like"]:<60}")
        print(f"{'Wind Speed':<30}{weather["wind"]["speed"]:<60}")
        print(f"{'Pressure':<30}{weather["main"]["pressure"]:<60}")
        print(f"{'Humidity':<30}{weather["main"]["humidity"]:<60}")
        print(f"{'Visibility':<30}{weather["visibility"]:<60}")
        print("-"*40)
    except Exception as e:
        logging.error(e)
        print("Something went wrong. Please try again later.")
        return None

def main():
    try:
        print("-"*40)
        print("Welcome to BRUIN weather forecast")
        print("-"*40)
        while True:
            try:
                print("Please select the look up by which you want to check weather forecast:")
                print("1. state & city")
                print("2. zip code")
                print("3. exit")
                user_choice = int(input("Please enter your choice: "))
                if user_choice == 1:
                    state_code = input("Please enter your state abbreviation e.g. NY: ").upper().strip()
                    if state_code.isalpha():
                        city_name = input("Please enter your city name: ").lower().strip()
                        if city_name.isalpha():
                            unit = input("Please enter unit as 'kelvin' or 'imperial' or 'metric': ").lower().strip()
                            if unit == 'imperial' or unit == 'metric' or unit == 'kelvin':
                                api_coordinates_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid={api_key}&units={unit}"
                                coordinates_list = get_coordinates(api_coordinates_url)
                                coordinates = coordinates_list[0]
                                weather = get_weather(coordinates, unit)
                                print_weather(weather)
                            else:
                                print("Please enter unit as 'standard' or 'fahrenheit' or 'celsius'.")
                        else:
                            print("Please enter a valid city name.")
                    else:
                        print("Please enter a valid state abbreviation.")
                elif user_choice == 2:
                    try:
                        zip_code = input("Please enter your 5 digit zipcode: ").strip()
                        if zip_code.isdigit():
                            unit = input("Please enter unit as 'kelvin'(standard) or 'imperial'(fahrenheit) or 'metric'(celsius): ").lower().strip()
                            if unit == 'imperial' or unit == 'metric' or unit == 'kelvin':
                                api_coordinates_url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}&units={unit}"
                                coordinates = get_coordinates(api_coordinates_url)
                                weather = get_weather(coordinates, unit)
                                print_weather(weather)
                            else:
                                print("Please enter unit as 'standard' or 'fahrenheit' or 'celsius'.")
                        else:
                            print("Please enter zip code in numbers only")
                    except requests.exceptions.RequestException as e:
                        print("Something went wrong. Please try again.")
                        logging.error(e)
                elif user_choice == 3:
                    print("Thank you for using BRUIN weather forecast")
                    break
            except ValueError:
                print("Please enter the suggested number")
                logging.error("Invalid input")
    except KeyboardInterrupt:
        print("\nYou chose to close the BRUIN weather forecast. See you next time!")

if __name__ == '__main__':
    main()