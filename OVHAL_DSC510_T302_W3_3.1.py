#------------------------------------------------------------
#DSC 510
#Week 3
#Programming Assignment Week 3
#Author Praful Ovhal
#09/16/2025

#Change#: 1
#Change(s) Made: float number precision set to 2
#Date of Change: 09/19/2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 09/19/2025

#Change#: 2
#Change(s) Made:
#   1. try except block added to catch the error
#   2. conditional statements added to calculate the cost by discounted rate
#Date of Change: 09/23/2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 09/26/2025
#--------------------------------------------------------------

print('\n Welcome to the BRUIN Services Ltd'
      + '\n Please enter your details below.')

company_name = input('\n What is your company name? : ')
cable_length = float(input('\n To install the Fibre Optic cable, please enter the length (in feet)? : '))

try:
    cost1 = 0.95  # Installation cost for cable length upto 100 feet
    cost2 = 0.85  # Installation cost for cable length more than 100 and upto 250 feet
    cost3 = 0.75  # Installation cost for cable length more than 250 and upto 500 feet
    cost4 = 0.55  # Installation cost for cable length more than 500 feet
    cost_applied = 0.00

    #Applying the cost per feet by checking the input cable length
    if 0 < cable_length <= 100:
        cost_applied = cost1
    elif 100 < cable_length <= 250:
        cost_applied = cost2
    elif 250 < cable_length <= 500:
        cost_applied = cost3
    elif cable_length > 500:
        cost_applied = cost4
    else:
        print('\n The length of the Optic fibre cable should be greater than 0 !')

    cost_fo_cable = cable_length * cost_applied                         #Calculating the total discounted cost to install the optic fibre cable per foot which is based on the cable length

    #Printing the receipt in the format below
    print('\n Here is your receipt:'
        + '\n ----------------------------------------------------------------------------'
        + '\n                              BRUIN Services Ltd'
        + '\n ----------------------------------------------------------------------------'
        + '\n Billing to:', company_name
        + '\n Total length of Fibre Optic cable used to install:', format(cable_length, ".2f"), 'feet'
        + '\n Discounted cost applied per feet:', format(cost_applied, ".2f")
        + '\n Total amount to pay: $', format(cost_fo_cable, ".2f"),
          '\n ----------------------------------------------------------------------------')
except:
    print('\n Please enter cable length in number format (like 123 or 12.21).\n Lets start again...')
