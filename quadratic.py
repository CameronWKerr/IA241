# Cameron Kerr and JT Scott IA 241
# quadratic.py
# program that computes the roots of a quadratic equation.
# Language: Python 3.9.1

# import math function
import math

# create and initialize variables to null
a = 0.0
b = 0.0
c = 0.0
discrim = 0.0
discRoot = 0.0
root1 = 0.0
root2 = 0.0

# message to users
print('This program finds the solutions to a quadratic equation.')

# input-get coefficients
a = float(input('\nPlease enter the coefficient (a): '))
b = float(input('\nPlease enter the coefficient (b): '))
c = float(input('\nPlease enter the coefficient (c): '))

# trap for bad input
if a == 0:
    print('The value of the coefficient (a) cannot be equal to 0')

# compute the discriminant
discrim = (b**2) - (4*a*c)

# check if the discriminant is positive, negative, or zero
# compute and display the root(s)
if discrim < 0:
    discrim = -discrim
    discRoot = math.sqrt(discrim)
    root1 = (-b + discRoot)/(2 * a)
    root2 = (-b + discRoot)/(2 * a)
    discRoot = format(discRoot, '0.2f')
    root1 = str(discRoot) + ' + i '
    root2 = str(discRoot) + ' - i '
    print("\nThis equation has complex roots: ", "-",root1, " and ", "-",root2)

elif discrim == 0:
    discRoot = math.sqrt(discrim)
    root1 = (-b + discRoot)/(2 * a)
    discRoot = format(discRoot, '0.2f')
    print("\nThe solution to the equation is: ", root1)
    
else:
    discRoot = math.sqrt(discrim)
    root1 = (-b + discRoot)/(2 * a)
    root2 = (-b - discRoot)/(2 * a)
    discRoot = format(discRoot, '0.2f')
    print("\nThe solutions to the equation are: ", root1, " and ", root2)
