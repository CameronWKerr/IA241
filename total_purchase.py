# Lab 3 Question 1 - Total Purchase
# Cameron Kerr
# Language: Python 3.9.1
# total_purchase.py

# create variables and initialize to null
item1=0.0
item2=0.0
item3=0.0
item4=0.0
item5=0.0
sales_tax=.06

# get input for variables
item1=float(input('What is the price of the first item purchased? '))
item2=float(input('What is the price of the second item purchased? '))
item3=float(input('What is the price of the third item purchased? '))
item4=float(input('What is the price of the fourth item purchased? '))
item5=float(input('What is the price of the fifth item purchased? '))

# add items together to calculate subtotal of sale
subtotal=item1+item2+item3+item4+item5

# print subtotal
print('The subtotal of the five items is $', \
      format(subtotal, '.2f'))

# factor in sales tax variable to get the total cost of sales tax
tax_total=subtotal*.06

# print total sales tax cost
print('The total sales tax cost of the five items is $',\
             format(tax_total, '.2f'))

# calculate the total cost
total=subtotal+tax_total

# print the total cost
print('The total cost of the five items is $',\
      format(total, '.2f'))
