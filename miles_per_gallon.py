# Lab 3 Question 2 - Miles-per-Gallon
# Cameron Kerr
# Language: Python 3.9.1
# miles_per_gallon.py

# create variables and initialize to null
miles_driven=0.0
gallons_used=0.0

# get input for variables
miles_driven=float(input('How many miles have you driven? '))
gallons_used=float(input('How much gas did you use? '))

# calculate MPG
MPG=miles_driven/gallons_used

# print results
print('Your car gets', format(MPG, '.2f'), 'miles per gallon.')
