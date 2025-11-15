#------------------------------------------------------------
#DSC 510
#Week 11
#Programming Assignment 11.1 -
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
from tabulate import tabulate

country_code = 'US'
api_key = "f577dc33e820ff8ed415cd0b7189ca33"
unit = "imperial"

# Error logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='error.log',  # Logs will be written to this file
    filemode='a'           # Append mode
)

def get_coordinates(api_coordinates_url):
    headers = {'cache-control': 'no-cache'}
    response = requests.get(api_coordinates_url, headers=headers)
    coordinates = json.loads(response.text)
    return coordinates

def get_weather(coordinates):
    latitude = coordinates['lat']
    longitude = coordinates['lon']
    api_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units={unit}"
    headers = {'cache-control': 'no-cache'}
    response = requests.get(api_weather_url, headers=headers)
    weather = json.loads(response.text)
    return weather

def print_weather(weather):
    print("-"*40)
    print(f"{'Parameters':<30}{'Values':<60}")
    print("-" * 40)
    print(f"{'City':<30}{weather["name"]:<60}")
    print(f"{'Cloud Coverage':<30}{weather["weather"][0]["main"]:<60}")
    print(f"{'Description':<30}{weather["weather"][0]["description"]:<60}")
    print(f"{'Current Temperature':<30}{weather["main"]["temp"]:<60} F")
    print(f"{'Max Temperature':<30}{weather["main"]["temp_max"]:<60} F")
    print(f"{'Min Temperature':<30}{weather["main"]["temp_min"]:<60} F")
    print(f"{'Feels Like':<30}{weather["main"]["feels_like"]:<60}")
    print(f"{'Wind Speed':<30}{weather["wind"]["speed"]:<60} m/h")
    print(f"{'Pressure':<30}{weather["main"]["pressure"]:<60} psi")
    print(f"{'Humidity':<30}{weather["main"]["humidity"]:<60} %")
    print(f"{'Visibility':<30}{weather["visibility"]:<60} mi\"")
    print("-"*40)

def main():
    try:
        print("-"*40)
        print("Welcome to BRUIN weather forecast")
        print("-"*40)
        while True:
            print("Please select the look up by which you want to check weather forecast:")
            print("1. state & city")
            print("2. zip code")
            print("3. exit")
            user_choice = int(input("Please enter your choice: "))
            if user_choice == 1:
                state_code = input("Please enter your state abbreviation e.g. NY: ")
                city_name = input("Please enter your city name: ")
                api_coordinates_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid={api_key}"
                coordinates_list = get_coordinates(api_coordinates_url)
                coordinates = coordinates_list[0]
                weather = get_weather(coordinates)
                print_weather(weather)
            elif user_choice == 2:
                zip_code = input("Please enter your zipcode: ")
                api_coordinates_url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"
                coordinates = get_coordinates(api_coordinates_url)
                weather = get_weather(coordinates)
                print_weather(weather)
            elif user_choice == 3:
                print("Thank you for using BRUIN weather forecast")
                break
    except KeyboardInterrupt:
        print("\nYou chose to close the BRUIN weather forecast. See you next time!")

if __name__ == '__main__':
    main()