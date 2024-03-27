#Cameron Kerr
#mass_and_weight.py
#language: Python 3.9.1

# create and initialize variables to null
mass=0.0
GRAVITY=9.8

# get mass input
mass=float(input('What is the mass of the object? '))

# calculate using the equation
weight=mass * GRAVITY

# decision block
if weight>500:
    print('This object is too heavy')
elif weight<100:
    print('This object is too light')
else:
    print('This object is within the acceptable range. \nThe weight of the object \
is', format(weight,'.2f'), 'newtons')

