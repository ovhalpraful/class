#------------------------------------------------------------
#DSC 510
#Week 6
#Programming Assignment 6.1 - Accepting temperaturess and finding the smallest & largest in the list
#Author Praful Ovhal
#Date 10-14-2025

#Change#: 1
#Change(s) Made: Added comments and formatted the output
#Date of Change: 10-15-2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 10-15-2025
#--------------------------------------------------------------
import logging

# Error logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='error.log',  # Logs will be written to this file
    filemode='a'           # Append mode
)

def main():
    sentinel = 'q'
    temperatures = []

    #Accepting temperatures from the user
    while True:
        try:
            user_input = input("Enter the temperature in fahrenheit OR Press q to quit: ").strip()
            if user_input.lower() == sentinel:
                break
            temp = float(user_input)
            temperatures.append(temp)
        except ValueError as e:
            logging.error(f"Invalid input:{e}", exc_info=True)
            print("Please enter a valid temperature in numbers")
        except KeyboardInterrupt as e:
            logging.error(f"User interrupted:{e}", exc_info=True)
            exit("\nExiting the program...")

    #Finding the minimum, maximum, & total count of temperature from the list
    if temperatures:
        maximum_temp = max(temperatures)
        minimum_temp = min(temperatures)
        count = len(temperatures)
        print("\nYou have entered %d temperature value(s)" % count)
        print("Here are the temperatures you have entered:", [round(temperatures, 2) for temperatures in temperatures])
        print(f"The maximum temperature in the list is", format(maximum_temp, '.2f'),"\u00B0F")
        print(f"The minimum temperature in the list is", format(minimum_temp, '.2f'),"\u00B0F")
    else:
        print("No temperature(s) entered. Thank you for using this program.")

if __name__ == '__main__':
    main()