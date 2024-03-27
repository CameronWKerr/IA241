# Cameron Kerr
# Language: Python 3.9.1
# lab5_problem1.py

# This program will write a program that displays a table of the Celcius
# temperatures 0 through 20 and their Fahrenheit equivalents.

# create and initialize variables to null
celsius = 0.0
fahrenheit = 0.0

# create and print the table headings
print('Celsius\t\tFahrenheit')
print('------------------------------------')

# convert Celsius temps. 0-20 to Fahrenheit
for celsius in range(0, 21):
    fahrenheit = 9/5 * celsius + 32
    print(format(celsius, '0.2f'), '\t\t', format(fahrenheit, '0.2f'))
