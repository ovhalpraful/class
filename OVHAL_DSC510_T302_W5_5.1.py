#------------------------------------------------------------
#DSC 510
#Week 5
#Programming Assignment Week 5
#Author Praful Ovhal
#Date 10-08-2025
#--------------------------------------------------------------

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

def calculate_average():
    try:
        number_range = int(input('\n Please enter total count of numbers: '))

        if number_range <= 0:
            print("\n Please enter a number greater than zero and try again.")

        total = 0.0
        for count in range(int(number_range)):
            while True:
                try:
                    number = float(input(f"\n Please enter {count+1} number: "))
                    total = total + float(number)
                    break
                except ValueError:
                    print("\n Please enter a valid number and try again.")

        average = total / number_range
        return average
    except ValueError:
        print("\n Please enter a valid number and try again.")
        return None



def main():
    print("\n Welcome to Python Calculator")

    while True:
        print("\n Choose an operation: ")
        print("\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Average \n 6.Exit ")

        try:
            choice = input('\n Please enter your choice as (1 or 2 or 3 or 4 or 5 or 6): ').strip()

            if choice == '1':
                result = perform_calculations('+')
                print(f"\n The addition result is: {result}")
            elif choice == '2':
                result = perform_calculations('-')
                print(f"\n The subtraction result is: {result}")
            elif choice == '3':
                result = perform_calculations('*')
                print(f"\n The multiplication result is: {result}")
            elif choice == '4':
                result = perform_calculations('/')
                print(f"\n The division result is: {result}")
            elif choice == '5':
                result = calculate_average()
                print(f"\n The average result is: {result}")
            elif choice == '6':
                exit()
            else:
                print("\n Invalid choice. Please try again.")
        except ValueError:
            print("\n Please enter a valid choice and try again.")

if __name__ == '__main__':
    main()