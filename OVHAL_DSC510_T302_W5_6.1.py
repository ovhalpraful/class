#------------------------------------------------------------
#DSC 510
#Week 6
#Programming Assignment 6.1 - Accepting temperatures and finding the smallest & largest in the list
#Author Praful Ovhal
#Date 10-14-2025

#Change#: 1
#Change(s) Made: Added comments and formatted the output
#Date of Change: 10-15-2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 10-15-2025
#--------------------------------------------------------------

def main():
    sentinel = 'q'
    temperature = []

    #Accepting temperatures from the user
    while True:
        try:
            user_input = input("Enter the temperature in fahrenheit OR Press q to quit: ")
            if user_input.lower() == sentinel:
                break
            temp = float(user_input)
            temperature.append(temp)
        except ValueError:
            print("Please enter a valid temperature in numbers")
        except KeyboardInterrupt:
            exit("\nExiting the program...")

    #Finding the minimum, maximum, & total count of temperature in the list
    if temperature:
        maximum_temp = max(temperature)
        minimum_temp = min(temperature)
        count = len(temperature)
        print("\nYou have entered %d temperature value(s)" % count)
        print("Here are the temperatures you have entered:", [round(temperature, 2) for temperature in temperature])
        print(f"The maximum temperature in the list is", format(maximum_temp, '.2f'),"\u00B0F")
        print(f"The minimum temperature in the list is", format(minimum_temp, '.2f'),"\u00B0F")
    else:
        print("No temperature(s) entered. Thank you for using this program.")

if __name__ == '__main__':
    main()