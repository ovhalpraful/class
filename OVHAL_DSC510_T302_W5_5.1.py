#------------------------------------------------------------
#DSC 510
#Week 5
#Programming Assignment Week 5
#Author Praful Ovhal
#Date 10-08-2025
#--------------------------------------------------------------

def perform_calculations(operation):
    operation = input('\n What kind of calculation do you want to perform? Please enter the symbol: \n 1. for Add + \n 2.for Subtract - \n 3. for Multiply * \n 4.for Divide / \n >>')
    operand_1 = float(input('\n Please enter first operand? : '))
    operand_2 = float(input('\n Please enter second operand? : '))
    
    if operation == '+':
        addition = operand_1 + operand_2
        print(f"\n Addition result: {addition}")
        exit()
    if operation == '-':
        substraction = operand_1 - operand_2
        print(f"\n Substraction result: {addition}")
        exit()
    if operation == '*':
        multiplication = operand_1 * operand_2
        print(f"\n Multiplication result: {multiplication}")
        exit()
    if operation == '/':
        division = operand_1 / operand_2
        print(f"\n Division result: {division}")
        exit()

def calculate_average():
    numbers = input('\n Please total number of numbers you want : ')
    count = 0
    values = []



def main():
    choice = input("\n Please select the operation that you wish to perform. \n For Calculation enter C and for Average enter A \n >>")
    if choice == 'C':
        perform_calculations()
    if choice == 'A':
        calculate_average()

if __name__ == '__main__':
    main()