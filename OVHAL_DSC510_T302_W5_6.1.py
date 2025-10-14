#------------------------------------------------------------
#DSC 510
#Week 6
#Programming Assignment 6.1 - Accepting temperatures and finding the smallest & largest
#Author Praful Ovhal
#Date 10-14-2025
from decorator import append


#Change#: 1
#Change(s) Made:
#Date of Change:
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production:
#--------------------------------------------------------------

def main():
    sentinel = 'q'
    temperature = []
    while True:
        user_input = input("Enter the temperature in fahrenheit OR Press q to quit: ")

        if user_input.lower() == sentinel:
            break
        try:
            temp = float(user_input)
            temperature.append(temp)
        except ValueError:
            print("Please enter a valid temperature in numbers")
        except KeyboardInterrupt:
            print("Exiting the program...")
            break

    print("\n Here are the temperatures you have entered:", temperature)

    maximum_temp = max(temperature)
    minimum_temp = min(temperature)
    count = len(temperature)

    print("\n You have entered %d temperature value(s)" % count)
    print("\n The maximum temperature in the list is %g\u00B0F" % maximum_temp)
    print("\n The minimum temperature in the list is %g\u00B0F" % minimum_temp)

if __name__ == '__main__':
    main()