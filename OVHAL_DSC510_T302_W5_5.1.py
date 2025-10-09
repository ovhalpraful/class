#------------------------------------------------------------
#DSC 510
#Week 5
#Programming Assignment 5.1 - To perform math operations using looping
#Author Praful Ovhal
#Date 10-08-2025

#Change#: 1
#Change(s) Made: Added the runtime error handling code & comments
#Date of Change: 10/09/2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 10/09/2025
#--------------------------------------------------------------

# Function to calculate math operations.
def perform_calculations(operation):
    try:
        num1 = float(input('\n Please enter first number: '))
        num2 = float(input('\n Please enter second number: '))
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("\n Division by zero is not possible. Please try again.")
            else:
                return num1 / num2
        else:
            print("\n Operation not recognized. Please try again.")
    except ValueError:
        print("\n Please enter a valid number and try again.")
        return None

# Function to calculate average
def calculate_average():
    try:
        number_range = int(input('\n Please enter total count of numbers: '))
        if number_range > 0:
            total = 0.0
            for count in range(int(number_range)):      #Looping through the range & adding the numbers
                while True:
                    try:
                        number = float(input(f"\n Please enter {count+1} number: "))
                        total = total + float(number)
                        break
                    except ValueError:
                        print("\n Please enter a valid number and try again.")
            average = total / number_range
            return average
        else:
            print("\n Please enter a number greater than zero and try again.")
    except ValueError:
        print("\n Please enter a valid number and try again.")
        return None

def main():
    print("\n Welcome to Python Calculator")

    while True:
        print("\n Choose an operation: ")
        print("\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Average \n 6.Exit ")
        try:
            choice = int(input("\n Please enter your choice as (1 or 2 or 3 or 4 or 5 or 6): "))
            # Selecting an option from the choices
            if choice == 1:
                result = perform_calculations('+')
                print(f"\n The addition result is:", format(result,".2f"))
            elif choice == 2:
                result = perform_calculations('-')
                print(f"\n The subtraction result is:", format(result,".2f"))
            elif choice == 3:
                result = perform_calculations('*')
                print(f"\n The multiplication result is:", format(result,".2f"))
            elif choice == 4:
                result = perform_calculations('/')
                if result is not None:
                    print(f"\n The division result is:", format(result,".2f"))
                else:
                    print("\n The division result is None")
            elif choice == 5:
                result = calculate_average()
                # Handling runtime error
                if result is None:
                    print(f"\n The average result is: {result}")
                else:
                    print(f"\n The average result is:", format(result, ".2f"))
            elif choice == 6:
                print("\n Exiting...")
                exit()
            else:
                print("\n Invalid choice. Please try again.")
        except ValueError:
            print("\n Please enter a valid choice and try again.")
        # Handling the exception while terminating the program
        except KeyboardInterrupt:
            print("\n Exiting calculator...")
            exit()

if __name__ == '__main__':
    main()