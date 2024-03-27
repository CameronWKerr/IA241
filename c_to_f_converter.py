# Lab 3 Question 3 - Celsius to Fahrenheit Temperature Converter
# Cameron Kerr
# Language: Python 3.9.1
# c_to_f_converter.py

# create variable and initialize to null
C=0.0

# get input for variable
C=float(input('Enter a temperature in degrees Celsius '))

# convert to Fahrenheit
F = 9/5 * C + 32

# print results
print('The temperature you entered in degrees Celcius convers to', \
      format(F, '.2f'), 'degrees Fahrenheit.')
