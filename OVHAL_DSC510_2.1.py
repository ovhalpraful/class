#------------------------------------------------------------
#DSC 510
#Week 2
#Programming Assignment Week 2
#Author Praful Ovhal
#09/16/2025

#Change#:
#Change(s) Made:
#Date of Change:
#Author:
#Change Approved by:
#Date Moved to Production:
#--------------------------------------------------------------

print('\n Welcome to the BRUIN Services Ltd'
      + '\n Please enter your details below.')

company_name = input('\n What is your company name? : ')
fo_cable_length = float(input('\n To install the Fibre Optic cable, please enter the length (in feet)? : '))

installation_cost = 0.95                                     #Installation cost per feet
cost_fo_cable = fo_cable_length * installation_cost          #Calculating the cost to install the optic fibre cable per foot

#Printing the receipt in the format below
print('\n Here is your receipt:'
    + '\n ----------------------------------------------------------------------------'
    + '\n                              BRUIN Services Ltd'
    + '\n ----------------------------------------------------------------------------'
    + '\n Billing to:',company_name
    + '\n Total length of Fibre Optic cable used to install:',fo_cable_length,'feet'
    + '\n Total amount to pay: $',cost_fo_cable,
      '\n ----------------------------------------------------------------------------')
