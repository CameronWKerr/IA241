# Calculate the area of a circle
# Cameron Kerr IA 241
# Language: Python 3.9.1
# area_of_circle.py

#create and initialize variables and constants
radius = 0.0
area = 0.0
PI = 3.14

#input - get the radius of the circle
radius = float(input('Enter the radius of the circle '))

#process - compute the area of the circle
area = (PI * radius ** 2)

#output - display the result
print('The area of the circle is', format(area, '.2f'))
